from pathlib import Path
from typing import List

import wx

from GameStage import GameStage
from LoadingBar import LoadingBar
from Particle import Particle
from Profiler import profiler

from units.NormalUnit import NormalUnit
from units.UnitBase import UnitBase

from windows.WindowBase import WindowBase


class App(wx.App):

	playing: bool = True
	units: List[UnitBase] = []
	particles: List[Particle] = []
	windows: List[WindowBase] = []
	loadBar: LoadingBar
	gameStage: GameStage
	runner: wx.Timer
	colordb: wx.ColourDatabase

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
		import sys
		if not getattr(sys, 'FROZEN', False):
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
			profiler.startState( 'tick_stage' )
			self.gameStage.Tick()
			profiler.stopState( 'tick_stage' )
			profiler.startState( 'tick_windows' )
			for window in self.windows:
				window.OnTick()
			profiler.stopState( 'tick_windows' )
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


if __name__ == '__main__':
	app = App()
	app.MainLoop()