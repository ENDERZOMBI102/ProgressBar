from time import time

import wx

from BaseClasses import Drawable, Tickable
from GameStage import GameStage


class Particle(Drawable, Tickable):

	pos: wx.Point
	direction: int
	speed: int
	moveTimer: float

	def __init__(self, pos: wx.Point, direction: int, speed: int):
		self.pos = pos
		self.direction = direction
		self.speed = speed
		self.moveTimer = time()

	def OnDraw( self, stage: GameStage ):
		pass

	def OnTick( self ):
		if time() - self.moveTimer > self.speed * 0.0020:
			x, y = self.pos.Get()
			self.pos = wx.Point( x + 0, y + 10 )
			self.moveTimer = time()
