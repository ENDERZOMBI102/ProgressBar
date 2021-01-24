from time import time

from LoadingBar import LoadingBar
from unit.UnitBase import UnitBase
from unit.behavior.BehaviorBase import BehaviorBase


class FollowBehavior(BehaviorBase):

	followTimer: float

	def __init__( self, unit: UnitBase ):
		super().__init__(unit)
		self.followTimer = time()

	def Think( self, player: LoadingBar, stage: 'GameStage'):
		if time() - self.moveTimer > self.unit.speed * 0.0020:
			offset: int = 0
			# follow player X?
			if time() - self.followTimer > 0.20:
				if self.unit.bbox.GetRight() < player.GetRect().GetRight():
					offset = 10
				else:
					offset = -10
				self.followTimer = time()
			self.unit.bbox.Offset( offset, 10 )
			self.moveTimer = time()
