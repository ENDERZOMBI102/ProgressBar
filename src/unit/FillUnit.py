import wx

from .UnitBase import UnitBase
from .behavior.BehaviorBase import BehaviorBase


class FillUnit(UnitBase):

	def __init__(self, pos: wx.Point, speed: int, behavior: BehaviorBase.__class__):
		super( FillUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#37ED8B'),
			behavior=behavior(self)
		)

	def OnBarTouch( self, bbox: wx.Rect ) -> None:
		if self.loadBar.IsScore(self.bbox):
			self.loadBar.AddScore( 100 )
			self.Remove()
		else:
			self.Kill()

