import wx

from BaseClasses import Interactable, Drawable, Collidable, Entity
from Util import MouseButton


class DistractionBase( Entity, Interactable, Collidable, Drawable ):

	bbox: wx.Rect
	dc: wx.WindowDC
	removed = False

	def __init__(self, pos: wx.Point):
		self.dc = wx.WindowDC(self)
		self.bbox = wx.Rect( pos, wx.Size(100, 200) )

	def GetBBox( self ) -> wx.Rect:
		return self.bbox

	def OnTouch( self, bbox: wx.Rect ) -> None:
		pass

	def OnClick( self, pos: wx.Point, btn: MouseButton ) -> None:
		self.removed = True

	def OnDraw( self, canvas: wx.WindowDC ) -> None:
		canvas.DrawRectangle( self.bbox )
