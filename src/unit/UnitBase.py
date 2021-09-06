import wx

from LoadingBar import LoadingBar
from BaseClasses import Tickable, Drawable, Entity, Interactable
from Util import MouseButton


class UnitBase(Entity, Tickable, Drawable, Interactable):

	color: wx.Colour
	bbox: wx.Rect
	removed: bool = False
	behavior: 'BehaviorBase'
	loadBar: LoadingBar

	def __init__(self, pos: wx.Point, speed: int, color: wx.Colour, behavior):
		self.color = color
		self.speed = speed
		self.behavior = behavior
		self.bbox = wx.Rect( pos, wx.Size(20, 40) )
		self.loadBar = wx.GetApp().loadBar

	def SetColor( self, color: str ):
		self.color = wx.GetApp().GetColor(color)

	def OnTick( self, tickDelta: float ):
		if not self.removed:
			self.behavior.Think( self.loadBar, wx.GetApp().gameStage )
			if self.bbox.GetY() >= wx.GetApp().gameStage.GetSize().GetHeight():
				self.Remove()

	def OnTouch( self, bbox: wx.Rect ) -> None:
		self.OnCollide(bbox)

	def OnCollide( self, bbox: wx.Rect ):
		pass

	def OnClick( self, pos: wx.Point, btn: MouseButton ) -> None:
		pass

	def GetBBox( self ) -> wx.Rect:
		return self.bbox

	def OnDraw( self, canvas: wx.WindowDC ):
		canvas.SetBrush( wx.Brush( self.color ) )
		canvas.SetPen( wx.Pen( self.color ) )
		canvas.DrawRectangle( self.bbox )

	def Kill( self ):
		self.Remove()

	def Remove( self ):
		self.removed = True
