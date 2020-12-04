from time import time

import wx

from .UnitBase import UnitBase


class FillUnit(UnitBase):

	def __init__(self, pos: wx.Point, speed: int):
		super( FillUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.Colour('#37ED8B')
		)

	def OnBarTouch( self ):
		if self.bar.IsScore(self):
			self.bar.score += 100
			self.bar.UpdateScore()
		self.Destroy()

