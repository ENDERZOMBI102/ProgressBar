from time import time
import random
import json
from pathlib import Path

import wx
from wx.lib.mixins.inspection import InspectionMixin

from LoadingBar import LoadingBar
from Event import TickEvent
from units.FillUnit import FillUnit
from units.JollyUnit import JollyUnit
from units.MalusUnit import MalusUnit
from units.MultiUnit import MultiUnit
from units.UnitBase import UnitBase
from units.NormalUnit import NormalUnit
from units.WrongUnit import WrongUnit
from units.ErrorUnit import ErrorUnit


class App(wx.App, InspectionMixin):

	unit: LoadingBar
	spawnTimer = time()
	playing: bool = True

	def OnPreInit(self):
		cfg = Path('./ProgressBar.cfg')
		if not cfg.exists():
			cfg.touch()
			with cfg.open('w') as file:
				json.dump({'record': 0, 'darkmode': False}, file)

	def OnInit(self):
		self.Init()
		# self.ShowInspectionTool()
		self.unit = LoadingBar()
		with open('./ProgressBar.cfg', 'r') as file:
			options = json.load(file)
			self.unit.record = options[ 'record' ]
			self.unit.darkmode = options[ 'darkmode' ]
		self.unit.UpdateColor()
		self.unit.UpdateRecord()
		self.unit.Show()
		wx.CallLater( 100, self.Tick )
		return True

	def OnExit(self):
		with open('./ProgressBar.cfg', 'w') as file:
			json.dump({'record': self.unit.record, 'darkmode': self.unit.darkmode}, file)
		return True

	def Tick( self ):
		if self.playing:
			if time() - self.spawnTimer > random.randrange(0, 4) * random.randrange(1, 3):
				self.spawnTimer = time()
				self.Spawn()
			# move units
			for obj in self.unit.GetChildren():
				if isinstance(obj, UnitBase):
					if not obj.removed:
						wx.PostEvent( obj, TickEvent() )
		wx.CallLater( 10, self.Tick )

	def KillUnits( self ):
		for obj in self.unit.GetChildren():
			if isinstance( obj, UnitBase ):
				if not obj.removed:
					obj.Destroy()

	def Spawn( self ):
		if len( self.unit.GetChildren() ) < 30:
			n = random.randrange(100)
			if n > 90:
				ErrorUnit(
					pos=randPos(),
					speed=random.randrange( 2, 4 )
				)
			elif n > 70:
				WrongUnit(
					pos=randPos(),
					speed=random.randrange( 2, 4 )
				)
			elif n > 40:
				NormalUnit(
					pos=randPos(),
					speed=random.randrange( 2, 4 )
				)
			elif n > 30:
				MalusUnit(
					pos=randPos(),
					speed=random.randrange( 2, 4 )
				)
			elif n > 20:
				MultiUnit(
					pos=randPos(),
					speed=random.randrange( 2, 4 ),
					scoreMultiplier=random.randrange( 0, 3 )
				)
			elif n > 13:
				JollyUnit(
					pos=randPos(),
					speed=random.randrange( 2, 4 ),
					initialState=random.randrange( 0, 5 )
				)
			elif n > 9:
				FillUnit(
					pos=randPos(),
					speed=random.randrange( 2, 4 )
				)


def randPos() -> wx.Point:
	size = wx.GetDisplaySize().Get()
	return wx.Point( random.randrange( 0, size[0] ), -40 )


if __name__ == '__main__':
	app = App()
	app.MainLoop()