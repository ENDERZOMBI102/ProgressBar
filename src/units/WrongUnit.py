import wx

from .UnitBase import UnitBase


class WrongUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int):
		super(WrongUnit, self).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#FCBA03')
		)

	def OnBarTouch( self, bbox: wx.Rect ) -> None:
		if self.loadBar.IsScore( self.bbox ):
			self.loadBar.score -= 5
			self.loadBar.UpdateScore()
			self.Remove()
		else:
			self.Kill()
