import wx


class Tickable:

	def OnTick( self ) -> None:
		pass


class Drawable:

	def OnDraw( self, canvas: wx.WindowDC ) -> None:
		pass


class Interactable:

	def OnBarTouch( self, bbox: wx.Rect ) -> None:
		pass


class Collidable:

	def OnCollide( self, bbox: wx.Rect ) -> None:
		pass
