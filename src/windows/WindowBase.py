import wx


class WindowBase(wx.Frame):

	pos: wx.Point
	size: wx.Size = wx.Size(100, 200)
	dc: wx.WindowDC

	def __init__(self, pos: wx.Point, title: str = 'Distraction'):
		super(WindowBase, self).__init__(
			parent=wx.GetApp().gameStage,
			pos=pos,
			size=self.size,
			title=title,
			style=wx.BORDER_NONE | wx.FRAME_NO_TASKBAR
		)
		self.pos = pos
		self.dc = wx.WindowDC(self)
		self.dc.SetPen( wx.Pen( wx.GetApp().GetColor('WHITE') ) )
		self.dc.SetBrush( wx.Brush( wx.GetApp().GetColor('WHITE') ) )
		self.dc.DrawRectangle(0, 0, 100, 100)

		self.Show()
		self.Bind(wx.EVT_CLOSE, self.OnDestroy, self)

	def OnDestroy( self, evt: wx.CloseEvent ):
		wx.GetApp().windows.remove(self)
		self.Destroy()

	def OnTick( self ):
		self.SetPosition(self.pos)
		self.SetSize(self.size)
