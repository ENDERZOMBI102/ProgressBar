import wx

from Event import EVT_TICK


class UnitBase(wx.Frame):

	lastPos: wx.Point
	removed: bool = False

	def __init__(self, pos: wx.Point, speed: int, color: wx.Colour):
		super().__init__(
			parent=None,
			pos=pos,
			size=wx.Size(20, 40),
			style=wx.BORDER_NONE | wx.FRAME_NO_TASKBAR
		)
		self.SetBackgroundColour( color )
		self.lastPos = pos
		self.speed = speed
		self.Show()
		self.bar = wx.GetApp().unit
		self.Bind(EVT_TICK, self.OnTick)
		# wx.CallLater( 10, self.OnTick )

	def OnTick( self, evt ):
		if self.removed:
			return

		pos = self.GetPosition().Get()

		if wx.GetDisplaySize().Get()[ 1 ] < pos[ 1 ]:
			self.Destroy()
		else:
			self.SetPosition( wx.Point( pos[ 0 ], pos[ 1 ] + self.speed ) )
			if wx.GetApp().unit.IsTouching( self ):
				self.OnBarTouch()
		# wx.CallLater( 10, self.OnTick )

	def OnBarTouch( self ):
		pass

	def Destroy( self ):
		self.removed = True
		super(UnitBase, self).Destroy()
