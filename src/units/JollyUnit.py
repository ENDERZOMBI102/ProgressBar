from time import time

import wx

from .UnitBase import UnitBase


class JollyUnit(UnitBase):

	action: int = 0 # 0 = normal, 1 = wrong, 2 = error, 3 = fill, 4 = multi, 5 = malus
	changeActionTime: float

	def __init__(self, pos: wx.Point, speed: int):
		super( JollyUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.Colour('#0390FC')
		)
		self.changeActionTime = time()

	def OnTick( self, evt ):
		if time() - self.changeActionTime > 5:
			if self.action == 5:
				self.action = 0
			else:
				self.action	+= 1
			if self.action == 0:  # normal
				self.SetBackgroundColour( wx.Colour('#0390FC') )
			elif self.action == 1:  # wrong
				self.SetBackgroundColour( wx.Colour('#FCBA03') )
			elif self.action == 2:  # error
				self.SetBackgroundColour( wx.ColourDatabase().Find('RED') )
			elif self.action == 3:  # fill
				self.SetBackgroundColour( wx.Colour('#2FF5F1') )
			elif self.action == 4:  # multi
				self.SetBackgroundColour()
			else:  # malus
				self.SetBackgroundColour()
		super(JollyUnit, self).OnTick(evt)

	def OnBarTouch( self ):
		if self.action == 0:
			self.bar.score += 2
		elif self.action == 1:
			self.bar.score -= 5
		elif self.action == 2:
			pass
		elif self.action == 3:
			self.bar.score += 100
		elif self.action == 4:
			pass
		else:
			pass
		self.bar.UpdateScore()
		self.Destroy()

