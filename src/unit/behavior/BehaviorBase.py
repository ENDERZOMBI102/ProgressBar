from time import time

from LoadingBar import LoadingBar
from unit.UnitBase import UnitBase


class BehaviorBase:

	unit: UnitBase
	moveTimer: float = 0

	def __init__( self, unit: UnitBase):
		self.moveTimer = time()
		self.unit = unit

	def Think( self, player: LoadingBar, stage: 'GameStage'):
		pass
