import wx

from .UnitBase import UnitBase
from .behavior.BehaviorBase import BehaviorBase


class ErrorUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int, behavior: BehaviorBase.__class__):
		super(ErrorUnit, self).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('RED'),
			behavior=behavior(self)
		)

	def OnBarTouch( self, bbox: wx.Rect ) -> None:
		self.loadBar.EndGame()
