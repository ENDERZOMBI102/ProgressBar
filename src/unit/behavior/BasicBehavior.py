from time import time

from LoadingBar import LoadingBar
from unit.UnitBase import UnitBase
from unit.behavior.BehaviorBase import BehaviorBase


class BasicBehavior(BehaviorBase):

	def __init__( self, unit: UnitBase ):
		super().__init__(unit)

	def Think( self, player: LoadingBar, stage: 'GameStage'):
		if time() - self.moveTimer > self.unit.speed * 0.0020:
			self.unit.bbox.Offset( 0, 10 )
			self.moveTimer = time()
