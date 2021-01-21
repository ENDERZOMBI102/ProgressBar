import wx

from .UnitBase import UnitBase


class MultiUnit(UnitBase):

	def __init__(self, pos: wx.Point, speed: int, scoreMultiplier: int = 1):
		super( MultiUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#9DEFF2')
		)
		self.score = 5 * scoreMultiplier

	def OnBarTouch( self ):
		if self.loadBar.IsScore(self.bbox):
			self.loadBar.score += self.score
			self.Remove()
		else:
			self.Kill()

