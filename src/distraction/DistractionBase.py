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
		self.Raise()
		wx.GetApp().loadBar.Raise()
		print('distraction')

	def OnDestroy( self, evt: wx.CloseEvent ):
		wx.GetApp().windows.remove(self)
		self.Destroy()

	def OnTick( self ) -> None:
		pass

	def OnCollide( self, bbox: wx.Rect ) -> None:
		pass
