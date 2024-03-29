from time import time

import wx

from .UnitBase import UnitBase
from .behavior.BehaviorBase import BehaviorBase


class JollyUnit(UnitBase):

	action: int = 0  # 0 = normal, 1 = wrong, 2 = error, 3 = fill, 4 = multi, 5 = malus
	changeActionTime: float = None

	def __init__(self, pos: wx.Point, speed: int, behavior: BehaviorBase.__class__, initialState=0):
		super( JollyUnit, self ).__init__(
			pos=pos,
			speed=speed,
			color=wx.GetApp().GetColor('#0390FC'),
			behavior=behavior(self)
		)
		self.action = initialState

	def OnTick( self, tickDelta: float ):
		if ( self.changeActionTime is None ) or ( time() - self.changeActionTime > 3 ):
			if self.action == 5:
				self.action = 0
			else:
				self.action += 1
			if self.action == 0:  # normal
				self.SetColor( '#0390FC' )
			elif self.action == 1:  # wrong
				self.SetColor( '#FCBA03' )
			elif self.action == 2:  # error
				self.SetColor( 'RED' )
			elif self.action == 3:  # fill
				self.SetColor( '#37ED8B' )
			elif self.action == 4:  # multi
				self.SetColor( '#9DEFF2' )
			else:  # malus
				self.SetColor( '#D531E0' )
			self.changeActionTime = time()
		super(JollyUnit, self).OnTick(tickDelta)

	def OnCollide( self, bbox: wx.Rect ) -> None:
		if self.loadBar.IsScore(self.bbox):
			if self.action == 0:
				self.loadBar.AddScore( 5 )
			elif self.action == 1:
				self.loadBar.AddScore( -5 )
			elif self.action == 2:
				self.loadBar.EndGame()
			elif self.action == 3:
				self.loadBar.AddScore( 100 )
			elif self.action == 4:
				self.loadBar.AddScore( 20 )
			else:
				self.loadBar.AddScore( 5 )
			self.Remove()
		else:
			self.Kill()


