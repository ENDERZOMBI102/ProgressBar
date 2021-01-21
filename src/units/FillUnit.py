import wx

from .UnitBase import UnitBase


class FillUnit(UnitBase):

	def __init__(self, pos: wx.Point, speed: int):
		super( FillUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#37ED8B')
		)

	def OnBarTouch( self ):
		if self.loadBar.IsScore(self.bbox):
			self.loadBar.score += 100
			self.Remove()
		else:
			self.Kill()

