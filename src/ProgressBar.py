from pathlib import Path

import wx

from GameStage import GameStage
from LoadingBar import LoadingBar
from Profiler import profiler


class App(wx.App):
	playing: bool = True
	loadBar: LoadingBar
	gameStage: GameStage
	runner: wx.Timer
	colordb: wx.ColourDatabase
	distractionsEnabled: bool = True

	def OnInit(self):
		self.colordb = wx.ColourDatabase()
		self.gameStage = GameStage()
		self.loadBar = LoadingBar()
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
			profiler.startState( 'tick_stage' )
			self.gameStage.Tick()
			profiler.startState( 'tick_stage' )
			profiler.startState( 'tick_loading_bar' )
			self.loadBar.OnTick()
			profiler.startState( 'draw_stage' )
			self.gameStage.Draw()
			profiler.stopState( 'draw_stage' )
			profiler.stopState( 'tick' )

	def Close( self ):
		self.playing = False
		self.gameStage.ClearStage()
		self.runner.Stop()
		self.loadBar.Destroy()
		self.gameStage.Destroy()

	def GetColor( self, color: str ) -> wx.Colour:
		clr: wx.Colour = self.colordb.Find(color)
		if not clr.IsOk():
			self.colordb.AddColour(color, wx.Colour(color) )
			clr = self.colordb.Find( color )
		return clr


def GetStage() -> GameStage:
	return wx.GetApp().gameStage


if __name__ == '__main__':
	app = App()
	app.MainLoop()
