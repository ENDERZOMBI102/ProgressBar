import wx

from .UnitBase import UnitBase


class NormalUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int):
		super( NormalUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.Colour('#0390FC')
		)

	def OnBarTouch( self ):
		if self.bar.IsScore(self):
			self.bar.score += 5
			self.bar.UpdateScore()
		self.Destroy()
