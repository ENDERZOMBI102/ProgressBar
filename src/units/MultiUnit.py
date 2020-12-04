from time import time

import wx

from .UnitBase import UnitBase


class MultiUnit(UnitBase):

	def __init__(self, pos: wx.Point, speed: int, scoreMultiplier: int = 1):
		super( MultiUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.Colour('#9DEFF2')
		)
		self.score = 5 * scoreMultiplier

	def OnBarTouch( self ):
		if self.bar.IsScore(self):
			self.bar.score += self.score
			self.bar.UpdateScore()
		self.Destroy()

