import wx

from .UnitBase import UnitBase


class ErrorUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int):
		super(ErrorUnit, self).__init__(
			pos=pos,
			speed=speed,
			color=wx.ColourDatabase().Find('RED')
		)

	def OnBarTouch( self ):
		if self.bar.IsScore( self ):
			self.bar.EndGame()
