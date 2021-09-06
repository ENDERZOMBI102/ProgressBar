import wx

from .UnitBase import UnitBase
from .behavior.BehaviorBase import BehaviorBase


class WrongUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int, behavior: BehaviorBase.__class__):
		super(WrongUnit, self).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#FCBA03'),
			behavior=behavior(self)
		)

	def OnCollide( self, bbox: wx.Rect ) -> None:
		if self.loadBar.IsScore( self.bbox ):
			self.loadBar.AddScore( -5 )
			self.Remove()
		else:
			self.Kill()
