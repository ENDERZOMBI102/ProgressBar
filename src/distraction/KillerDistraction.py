import wx

from .DistractionBase import DistractionBase


class KillerDistraction(DistractionBase):

	def __init__(self, pos: wx.Point):
		super(KillerDistraction, self).__init__(pos)
		self.dc.SetBrush( wx.Brush( wx.GetApp().GetColor('BLACK') ) )
		self.dc.DrawRectangle( self.GetRect() )

	def OnTick( self ) -> None:
		pass

	def OnCollide( self, bbox: wx.Rect ) -> None:
		wx.GetApp().loadBar.EndGame()
