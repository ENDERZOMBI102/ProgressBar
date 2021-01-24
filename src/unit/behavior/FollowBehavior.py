from time import time

from LoadingBar import LoadingBar
from unit.UnitBase import UnitBase
from unit.behavior.BehaviorBase import BehaviorBase


class FollowBehavior(BehaviorBase):

	followTimer: float = 0

	def __init__( self, unit: UnitBase ):
		super().__init__(unit)

	def Think( self, player: LoadingBar, stage: 'GameStage'):
		if time() - self.moveTimer > self.unit.speed * 0.0020:
			self.unit.bbox.Offset( 0, 10 )
			self.moveTimer = time()
			# follow player X?
			if time() - self.followTimer > 0.12:
				if self.unit.bbox.GetLeft() < player.GetRect().GetLeft():
					offset = -10
				else:
					offset = 10
				self.unit.bbox.Offset( offset, 0 )
				self.followTimer = time()
