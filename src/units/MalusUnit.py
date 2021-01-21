import wx

from .UnitBase import UnitBase


class MalusUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int):
		super(MalusUnit, self).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#D531E0')
		)

	def OnBarTouch( self ):
		if self.loadBar.IsScore( self.bbox ):
			self.loadBar.score -= 5
			self.loadBar.UpdateScore()
		else:
			self.Kill()
