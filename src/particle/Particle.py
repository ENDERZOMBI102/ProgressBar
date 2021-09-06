from time import time

import wx

from BaseClasses import Drawable, Tickable, Entity


class Particle(Entity, Drawable, Tickable):

	pos: wx.Point
	speed: int
	moveTimer: float

	def __init__(self, pos: wx.Point, speed: int):
		self.pos = pos
		self.speed = speed
		self.moveTimer = time()

	def OnDraw( self, canvas: wx.WindowDC ):
		pass

	def OnTick( self, tickDelta: float ):
		if time() - self.moveTimer > self.speed * 0.0020:
			x, y = self.pos.Get()
			self.pos = wx.Point( x + 0, y + 10 )
			self.moveTimer = time()
