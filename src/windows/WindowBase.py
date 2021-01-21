import wx

from GameStage import GameStage


class WindowBase(wx.Frame):

	def __init__(self, pos: wx.Point, title: str = 'Distraction'):
		super(WindowBase, self).__init__(
			parent=wx.GetApp().gameStage,
			pos=pos,
			size=wx.Size(100, 200),
			title=title,
			style=( wx.DEFAULT_FRAME_STYLE ^ wx.MINIMIZE_BOX ^ wx.MAXIMIZE_BOX ) | wx.FRAME_NO_TASKBAR
		)
		self.Show()
		self.Bind(wx.EVT_CLOSE, self.OnDestroy, self)

	def OnDestroy( self, evt: wx.CloseEvent ):
		wx.GetApp().windows.remove(self)
		self.Destroy()





