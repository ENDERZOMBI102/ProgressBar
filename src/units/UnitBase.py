from time import time

import wx

from Event import EVT_TICK


class UnitBase(wx.Frame):

	lastPos: wx.Point
	removed: bool = False

	def __init__(self, pos: wx.Point, speed: int, color: wx.Colour):
		super().__init__(
			parent=wx.GetApp().unit,
			pos=pos,
			size=wx.Size(20, 40),
			style=wx.BORDER_NONE | wx.FRAME_NO_TASKBAR
		)
		self.SetBackgroundColour( color )
		self.lastPos = self.GetScreenPosition()
		self.spawnTime = time()
		self.speed = speed
		self.bar = wx.GetApp().unit
		self.Show()
		self.Bind(EVT_TICK, self.OnTick)

	def OnTick( self, evt ):
		if self.removed:
			return
		self.HandleMove()

	def HandleMove( self ):
		pos = self.GetScreenPosition().Get()
		if wx.GetDisplaySize().Get()[ 1 ] - 20 < pos[ 1 ]:
			self.Destroy()
		else:
			self.Move( wx.Point( pos[ 0 ], pos[ 1 ] + self.speed ) )
			if self.GetScreenPosition() == self.lastPos:
				self.Destroy()
			else:
				self.lastPos = self.GetScreenPosition()
				if wx.GetApp().unit.IsTouching( self ):
					self.OnBarTouch()

	def OnBarTouch( self ):
		pass

	def Destroy( self ):
		self.removed = True
		super(UnitBase, self).Destroy()
