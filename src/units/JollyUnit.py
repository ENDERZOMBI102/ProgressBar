from time import time

import wx

from .UnitBase import UnitBase


class JollyUnit(UnitBase):

	action: int = 0  # 0 = normal, 1 = wrong, 2 = error, 3 = fill, 4 = multi, 5 = malus
	changeActionTime: float = None

	def __init__(self, pos: wx.Point, speed: int, initialState=0):
		super( JollyUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.Colour('#0390FC')
		)
		self.action = initialState

	def OnTick( self, evt ):
		if ( self.changeActionTime is None ) or ( time() - self.changeActionTime > 3 ):
			if self.action == 5:
				self.action = 0
			else:
				self.action += 1
			if self.action == 0:  # normal
				self.SetBackgroundColour( wx.Colour('#0390FC') )
			elif self.action == 1:  # wrong
				self.SetBackgroundColour( wx.Colour('#FCBA03') )
			elif self.action == 2:  # error
				self.SetBackgroundColour( wx.ColourDatabase().Find('RED') )
			elif self.action == 3:  # fill
				self.SetBackgroundColour( wx.Colour('#37ED8B') )
			elif self.action == 4:  # multi
				self.SetBackgroundColour( wx.Colour('#9DEFF2') )
			else:  # malus
				self.SetBackgroundColour( wx.Colour('#D531E0') )
			self.Refresh()
			self.changeActionTime = time()
		super(JollyUnit, self).OnTick(evt)

	def OnBarTouch( self ):
		if self.action == 0:
			self.bar.score += 5
		elif self.action == 1:
			self.bar.score -= 5
		elif self.action == 2:
			self.bar.EndGame()
			return
		elif self.action == 3:
			self.bar.score += 100
		elif self.action == 4:
			self.bar.score += 20
		else:
			self.bar.score -= 5
		self.bar.UpdateScore()
		self.Destroy()

