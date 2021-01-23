import wx

from .UnitBase import UnitBase


class NormalUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int):
		super( NormalUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#0390FC')
		)

	def OnBarTouch( self, bbox: wx.Rect ) -> None:
		if self.loadBar.IsScore(self.bbox):
			self.loadBar.score += 5
			self.Remove()
		else:
			self.Kill()
