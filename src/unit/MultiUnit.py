import wx

from .UnitBase import UnitBase
from .behavior.BehaviorBase import BehaviorBase


class MultiUnit(UnitBase):

	def __init__(self, pos: wx.Point, speed: int, behavior: BehaviorBase.__class__, scoreMultiplier: int = 1):
		super( MultiUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#9DEFF2'),
			behavior=behavior(self)
		)
		self.score = 5 * scoreMultiplier

	def OnBarTouch( self, bbox: wx.Rect ) -> None:
		if self.loadBar.IsScore(self.bbox):
			self.loadBar.score += self.score
			self.Remove()
		else:
			self.Kill()

