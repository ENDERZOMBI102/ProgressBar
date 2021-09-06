import wx

from .DistractionBase import DistractionBase


class KillerDistraction(DistractionBase):

	def __init__(self, pos: wx.Point):
		super(KillerDistraction, self).__init__(pos)

	def OnTick( self, tickDelta: float ) -> None:
		pass

	def OnTouch( self, bbox: wx.Rect ) -> None:
		wx.GetApp().loadBar.EndGame()
