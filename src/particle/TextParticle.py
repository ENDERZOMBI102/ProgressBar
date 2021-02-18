import wx

from GameStage import GameStage
from .Particle import Particle


class TextParticle(Particle):

	def __init__(self, pos: wx.Point, text: strs):
		super(TextParticle, self).__init__(pos: wx.Point, direction: int, speed: int)

	def OnDraw( self, stage: GameStage ):
		pass