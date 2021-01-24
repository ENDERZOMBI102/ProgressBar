import wx

from BaseClasses import Collidable, Tickable


class DistractionBase( wx.Frame, Tickable, Collidable ):

	size: wx.Size = wx.Size(100, 200)
	dc: wx.WindowDC

	def __init__(self, pos: wx.Point):
		super( DistractionBase, self ).__init__(
			parent=wx.GetApp().gameStage,
			pos=pos,
			size=self.size,
			style=wx.BORDER_NONE | wx.FRAME_NO_TASKBAR
		)
		self.dc = wx.WindowDC(self)
		self.dc.SetPen( wx.Pen( wx.GetApp().GetColor('GREEN') ) )
		self.dc.SetBrush( wx.Brush( wx.GetApp().GetColor('GREEN') ) )
		self.dc.DrawRectangle(0, 0, 100, 100)

		self.Show()
		self.Bind(wx.EVT_CLOSE, self.OnDestroy, self)

	def OnDestroy( self, evt: wx.CloseEvent ):
		wx.GetApp().windows.remove(self)
		self.Destroy()

	def OnTick( self ) -> None:
		state: wx.MouseState = wx.GetMouseState()
		if state.GetPosition().Get() == self.GetPosition().Get():
			if state.LeftIsDown():
				self.OnDestroy(None)

	def OnCollide( self, bbox: wx.Rect ) -> None:
		pass
