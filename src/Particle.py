import wx

from BaseClasses import Drawable, Tickable
from GameStage import GameStage


class Particle(Drawable, Tickable):

	pos: wx.Point
	color: wx.Colour

	def OnDraw( self, stage: GameStage ):
		pass

	def OnTick( self ):
		pass
