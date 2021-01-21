import random
from pathlib import Path
from time import time
from typing import List

import wx

from GameStage import GameStage
from LoadingBar import LoadingBar
from Particle import Particle
from Profiler import profiler

from units.ErrorUnit import ErrorUnit
from units.FillUnit import FillUnit
from units.JollyUnit import JollyUnit
from units.MalusUnit import MalusUnit
from units.MultiUnit import MultiUnit
from units.NormalUnit import NormalUnit
from units.NullUnit import NullUnit
from units.UnitBase import UnitBase
from units.WrongUnit import WrongUnit

from windows.WindowBase import WindowBase


class App(wx.App):

	playing: bool = True
	units: List[UnitBase] = []
	particles: List[Particle] = []
	windows: List[WindowBase] = []
	loadBar: LoadingBar
	gameStage: GameStage
	runner: wx.Timer
	spawnTimer = time()
	colordb: wx.ColourDatabase
	diffMultiplier: float = 1.0

	def OnInit(self):
		self.colordb = wx.ColourDatabase()
		self.gameStage = GameStage()
		self.loadBar = LoadingBar()
		self.units = [ NormalUnit( wx.Point(10, 10), 50 ) ]
		self.runner = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.Tick)
		wx.CallLater(90, self.runner.Start, 10)
		return True

	def OnExit(self):
		profiler.save( Path('./../profiling/latest.json') )
		return True

	def Tick( self, evt: wx.TimerEvent ):
		if self.playing:
			profiler.startState( 'tick' )
			profiler.startState( 'clear_window' )
			self.gameStage.clear()
			profiler.stopState( 'clear_window' )
			profiler.startState( 'remove_units' )
			for unit in self.units[::-1]:
				if unit.removed:
					self.units.remove(unit)
			profiler.stopState( 'remove_units' )
			profiler.startState( 'draw_units' )
			for unit in self.units:
				unit.OnDraw(self.gameStage)
			profiler.stopState( 'draw_units' )
			profiler.startState( 'tick_units' )
			for unit in self.units:
				unit.OnTick()
			profiler.stopState( 'tick_units' )
			profiler.startState( 'tick_loading_bar' )
			self.loadBar.OnTick()
			profiler.stopState( 'tick_units' )
			profiler.startState( 'particles' )
			for particle in self.particles:
				particle.OnDraw(self.gameStage)
			profiler.stopState( 'particles' )
			profiler.startState( 'spawning' )
			if time() - self.spawnTimer > ( random.randrange(1, 3) * random.randrange(1, 3) ) * self.diffMultiplier:
				self.spawnTimer = time()
				self.Spawn()
				if self.diffMultiplier > 0.1:
					self.diffMultiplier -= 0.01
			profiler.stopState( 'spawning' )
			profiler.stopState( 'tick' )

	def Close( self ):
		self.playing = False
		self.units.clear()
		self.runner.Stop()
		self.loadBar.Destroy()
		self.gameStage.Destroy()

	def GetColor( self, color: str ) -> wx.Colour:
		clr: wx.Colour = self.colordb.Find(color)
		if not clr.IsOk():
			self.colordb.AddColour(color, wx.Colour(color) )
			clr = self.colordb.Find( color )
		return clr

	def Spawn( self ):
		if len( self.units ) < 30:
			n = random.randrange(100)
			if n > 90:
				self.units.append(
					ErrorUnit(
						pos=randUnitPos(),
						speed=random.randrange( 2, 10 )
					)
				)
			elif n > 70:
				self.units.append(
					WrongUnit(
						pos=randUnitPos(),
						speed=random.randrange( 2, 10 )
					)
				)
			elif n > 40:
				self.units.append(
					NormalUnit(
						pos=randUnitPos(),
						speed=random.randrange( 2, 10 )
					)
				)
			elif n > 33:
				self.units.append(
					MalusUnit(
						pos=randUnitPos(),
						speed=random.randrange( 2, 10 )
					)
				)
			elif n > 26:
				self.units.append(
					NullUnit(
						pos=randUnitPos(),
						speed=random.randrange( 2, 10 )
					)
				)
			elif n > 20:
				self.units.append(
					MultiUnit(
						pos=randUnitPos(),
						speed=random.randrange( 2, 10 ),
						scoreMultiplier=random.randrange( 1, 3 )
					)
				)
			elif n > 13:
				self.units.append(
					JollyUnit(
						pos=randUnitPos(),
						speed=random.randrange( 2, 10 ),
						initialState=random.randrange( 0, 5 )
					)
				)
			elif n > 9:
				self.units.append(
					FillUnit(
						pos=randUnitPos(),
						speed=random.randrange( 2, 10 )
					)
				)
		if len( self.windows ) < 10:
			n = random.randrange( 100 )
			if n < 10:
				self.windows.append(
					WindowBase(
						pos=randWindowPos()
					)
				)


def randUnitPos() -> wx.Point:
	size = wx.GetDisplaySize().Get()
	return wx.Point( random.randrange( 0, size[0] ), -40 )


def randWindowPos() -> wx.Point:
	size = wx.GetDisplaySize().Get()
	return wx.Point( random.randrange( 0, size[0] ), random.randrange( 0, size[1] ) )


if __name__ == '__main__':
	app = App()
	app.MainLoop()