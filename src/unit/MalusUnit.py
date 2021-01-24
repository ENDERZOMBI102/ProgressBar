import wx

from .UnitBase import UnitBase
from .behavior.BehaviorBase import BehaviorBase


class MalusUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int, behavior: BehaviorBase.__class__):
		super(MalusUnit, self).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#D531E0'),
			behavior=behavior(self)
		)

	def OnBarTouch( self, bbox: wx.Rect ) -> None:
		if self.loadBar.IsScore( self.bbox ):
			self.loadBar.AddScore( -5 )
			self.Remove()
		else:
			self.Kill()
