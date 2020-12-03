from time import time
from typing import List
import random
import json
from pathlib import Path

import wx
from wx.lib.mixins.inspection import InspectionMixin

from Bar import Bar
from Event import EVT_TICK, TickEvent
from units.UnitBase import UnitBase
from units.Unit import Unit
from units.WrongUnit import WrongUnit
from units.ErrorUnit import ErrorUnit


class App(wx.App, InspectionMixin):

	unit: Bar
	units: List[UnitBase] = []
	spawnTimer = time()
	playing: bool = True

	def OnPreInit(self):
		cfg = Path('./ProgressBar.cfg')
		if not cfg.exists():
			cfg.touch()
			with cfg.open('w') as file:
				json.dump({'record': 0}, file)

	def OnInit(self):
		self.unit = Bar()
		with open('./ProgressBar.cfg', 'r') as file:
			self.unit.record = int( json.load(file)['record'] )
		self.unit.Show()
		wx.CallLater( 100, self.Tick )
		return True

	def OnExit(self):
		return True

	def Tick( self ):
		if self.playing:
			if time() - self.spawnTimer > random.randrange(0, 4):
				self.spawnTimer = time()
				self.Spawn()
			# remove destroyed units
			for obj in self.units:
				if obj.removed:
					del obj
			# move units
			for obj in self.units:
				if not obj.removed:
					wx.PostEvent(obj, TickEvent() )
		wx.CallLater( 10, self.Tick )

	def KillUnits( self ):
		for i in self.units:
			if not i.removed:
				i.Destroy()
		self.units.clear()

	def Spawn( self ):
		n = random.randrange(100)
		if n > 90:
			self.units.append( ErrorUnit( randPos(), random.randrange( 2, 4 ) ) )
		elif n > 70:
			self.units.append( WrongUnit( randPos(), random.randrange( 2, 4 ) ) )
		elif n > 40:
			self.units.append( Unit( randPos(), random.randrange( 2, 4 ) ) )


def randPos() -> wx.Point:
	size = wx.GetDisplaySize().Get()
	return wx.Point( random.randrange( 0, size[0] ), -40 )


if __name__ == '__main__':
	app = App()
	app.MainLoop()