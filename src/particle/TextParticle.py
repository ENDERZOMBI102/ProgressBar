import wx

from GameStage import GameStage
from .Particle import Particle


class TextParticle(Particle):

	text: str

	def __init__(self, pos: wx.Point, speed: int, text: str):
		super(TextParticle, self).__init__(pos, speed)
		self.text = text

	def OnDraw( self, stage: GameStage ):
		pass
