from abc import ABCMeta, abstractmethod

from GameStage import GameStage


class Tickable(metaclass=ABCMeta):

	@abstractmethod
	def OnTick( self ):
		pass


class Drawable(metaclass=ABCMeta):

	@abstractmethod
	def OnDraw( self, stage: GameStage ):
		pass