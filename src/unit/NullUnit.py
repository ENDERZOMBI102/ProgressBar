import wx

from .UnitBase import UnitBase
from .behavior.BehaviorBase import BehaviorBase


class NullUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int, behavior: BehaviorBase.__class__):
		super(NullUnit, self).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#969696'),
			behavior=behavior(self)
		)

	def OnBarTouch( self, bbox: wx.Rect ) -> None:
		if self.loadBar.IsScore( self.bbox ):
			self.Remove()
		else:
			self.Kill()
