import wx

from .UnitBase import UnitBase


class WrongUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int):
		super(WrongUnit, self).__init__(
			pos=pos,
			speed=speed,
			color=wx.Colour('#FCBA03')
		)

	def OnBarTouch( self ):
		if self.bar.IsScore( self ):
			self.bar.score -= 5
			self.bar.UpdateScore()
		self.Destroy()
