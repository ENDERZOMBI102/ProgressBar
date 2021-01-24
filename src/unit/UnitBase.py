import wx

from LoadingBar import LoadingBar
from BaseClasses import Tickable, Drawable, Interactable


class UnitBase(Tickable, Drawable, Interactable):

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

	def OnTick( self ):
		if not self.removed:
			self.behavior.Think( self.loadBar, wx.GetApp().gameStage )
			if self.loadBar.IsTouching(self.bbox):
				self.OnBarTouch( self.loadBar.GetRect() )
			if self.bbox.GetY() >= wx.GetApp().gameStage.GetSize().GetHeight():
				self.Remove()

	def OnDraw( self, canvas: wx.WindowDC ):
		canvas.SetBrush( wx.Brush( self.color ) )
		canvas.SetPen( wx.Pen( self.color ) )
		canvas.DrawRectangle( self.bbox )

	def Kill( self ):
		self.Remove()

	def Remove( self ):
		self.removed = True
