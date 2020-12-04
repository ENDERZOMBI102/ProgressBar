import wx

from .UnitBase import UnitBase


class MalusUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int):
		super(MalusUnit, self).__init__(
			pos=pos,
			speed=speed,
			color=wx.Colour('#D531E0')
		)

	def OnBarTouch( self ):
		if self.bar.IsScore( self ):
			self.bar.score -= 5
			self.bar.UpdateScore()
		self.Destroy()
