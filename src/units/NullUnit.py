import wx

from .UnitBase import UnitBase


class NullUnit( UnitBase ):

	def __init__(self, pos: wx.Point, speed: int):
		super(NullUnit, self).__init__(
			pos=pos,
			speed=speed,
			color=wx.Colour('#969696')
		)

	def OnBarTouch( self ):
		self.Destroy()
