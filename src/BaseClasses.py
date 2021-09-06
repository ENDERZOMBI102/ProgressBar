from abc import ABCMeta, abstractmethod

import wx

from Util import MouseButton


class Tickable(metaclass=ABCMeta):

	@abstractmethod
	def OnTick( self, tickDelta: float ) -> None:
		pass


class Drawable(metaclass=ABCMeta):

	@abstractmethod
	def OnDraw( self, canvas: wx.WindowDC ) -> None:
		pass


class Interactable(metaclass=ABCMeta):

	@abstractmethod
	def OnClick( self, pos: wx.Point, btn: MouseButton ) -> None:
		pass

	@abstractmethod
	def OnTouch( self, bbox: wx.Rect ) -> None:
		pass


class Collidable:
	pass


class Entity(metaclass=ABCMeta):

	removed: bool = False

	@abstractmethod
	def GetBBox( self ) -> wx.Rect:
		pass

