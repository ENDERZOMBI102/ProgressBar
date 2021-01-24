import wx

from .UnitBase import UnitBase
from .behavior.BasicBehavior import BasicBehavior
from .behavior.BehaviorBase import BehaviorBase


class NormalUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int, behavior: BehaviorBase.__class__):
		super( NormalUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#0390FC'),
			behavior=behavior(self)
		)

	def OnBarTouch( self, bbox: wx.Rect ) -> None:
		if self.loadBar.IsScore(self.bbox):
			self.loadBar.score += 5
			self.Remove()
		else:
			self.Kill()
