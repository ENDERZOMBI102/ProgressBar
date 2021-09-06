import random
from time import time
from typing import List, Union, Tuple

import wx
from PIL import ImageGrab

import Util
from BaseClasses import Entity, Interactable
from Profiler import profiler
from Score import ScoreData
from distraction.DistractionBase import DistractionBase
from distraction.KillerDistraction import KillerDistraction
from particle.Particle import Particle
from unit.UnitBase import UnitBase
from unit.ErrorUnit import ErrorUnit
from unit.FillUnit import FillUnit
from unit.JollyUnit import JollyUnit
from unit.MalusUnit import MalusUnit
from unit.MultiUnit import MultiUnit
from unit.NormalUnit import NormalUnit
from unit.NullUnit import NullUnit
from unit.WrongUnit import WrongUnit
from unit.behavior.BasicBehavior import BasicBehavior
from unit.behavior.BehaviorBase import BehaviorBase
from unit.behavior.FollowBehavior import FollowBehavior


class GameStage(wx.Frame):

	# draw data
	_screen: wx.Bitmap
	_dc: wx.WindowDC
	_now: float = time()
	_last: float = 0
	# stuff
	score: ScoreData
	app: 'ProgressBar'
	diffMultiplier: float = 1.0
	# entities
	entities: List[ Union[ Entity, Particle, UnitBase, DistractionBase ] ] = []

	def __init__(self):
		super(GameStage, self).__init__( None )
		self.InitScreen()
		self._dc = wx.WindowDC(self)

		self.app = wx.GetApp()

		self.ShowFullScreen(True)
		self.Raise()

		self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse, self)
		self.Bind(wx.EVT_SET_FOCUS, lambda evt: wx.GetApp().loadBar.Raise() if wx.GetApp().playing else print(end='') )

	def InitScreen( self ) -> None:
		disp: wx.Rect = wx.Display( wx.Display.GetFromWindow(self) ).GetGeometry()
		img = ImageGrab.grab( bbox=( disp.GetX(), disp.GetY(), disp.GetWidth(), disp.GetHeight() ) )
		wx_img = wx.Image( img.width, img.height, img.convert( 'RGB' ).tobytes() )
		if img.mode[ -1 ] == 'A':
			alpha = img.getchannel( "A" ).tobytes()
			wx_img.InitAlpha()
			for x in range( wx_img.GetWidth() ):
				for y in range( wx_img.GetHeight() ):
					wx_img.SetAlpha( x, y, alpha[ x + y * img.width ] )
		self._screen = wx_img.ConvertToBitmap()

	def ClearScreen( self ) -> None:
		self._dc.DrawBitmap( self._screen, 0, 0 )

	def ClearStage( self ) -> None:
		self.entities.clear()
		self.ClearScreen()

	def Tick( self ) -> None:
		# tick everything
		self._last, self._now = self._now, time()
		tickDelta = self._now - self._last
		profiler.startState( 'tick_entities' )
		for entity in self.entities:
			entity.OnTick(tickDelta)
		profiler.stopState( 'tick_entities' )
		profiler.startState( 'remove_entities' )
		for entity in self.entities[ ::-1 ]:
			if entity.removed:
				self.entities.remove( entity )
		profiler.stopState( 'remove_entities' )
		profiler.startState( 'spawn_entities' )
		if tickDelta > 4:
			self.SpawnUnit()
		if tickDelta > 5:
			self.SpawnDistraction()
		profiler.stopState( 'spawn_entities' )

	def Draw( self ) -> None:
		profiler.startState( 'clear_screen' )
		self.ClearScreen()
		profiler.stopState( 'clear_screen' )
		profiler.startState( 'draw_entities' )
		for entity in self.entities:
			entity.OnDraw(self._dc)
		profiler.stopState( 'draw_entities' )

	def OnMouse( self, evt: wx.MouseEvent ) -> None:
		if evt.GetButton() not in Util.IGNORED_MOUSE_BTN_LIST:
			clickPos: Tuple[ int, int ] = evt.GetPosition().Get()
			for entity in self.entities:
				if isinstance( entity, Interactable ) and entity.GetBBox().Contains( evt.GetPosition() ):
					entPos: Tuple[int, int] = entity.GetBBox().GetPosition().get()
					entity.OnClick(
						wx.Point( clickPos[0] - entPos[0], clickPos[1] - entPos[1] ),
						Util.MOUSE_BTN_LOOKUP[ evt.GetButton() ]
					)

	def SpawnDistraction( self ) -> None:
		n = random.randrange( 100 )
		if n < 10:
			self.entities.append(
				KillerDistraction(
					pos=randWindowPos()
				)
			)

	def SpawnUnit( self ) -> None:
		n = random.randrange( 100 )
		if n > 90:
			self.entities.append(
				ErrorUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)
		elif n > 70:
			self.entities.append(
				WrongUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)
		elif n > 40:
			self.entities.append(
				NormalUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)
		elif n > 33:
			self.entities.append(
				MalusUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)
		elif n > 26:
			self.entities.append(
				NullUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)
		elif n > 20:
			self.entities.append(
				MultiUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior(),
					scoreMultiplier=random.randrange( 1, 3 )
				)
			)
		elif n > 13:
			self.entities.append(
				JollyUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior(),
					initialState=random.randrange( 0, 5 )
				)
			)
		elif n > 9:
			self.entities.append(
				FillUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)


def randUnitPos() -> wx.Point:
	size = wx.GetDisplaySize().Get()
	return wx.Point( random.randrange( 0, size[ 0 ] ), -40 )


def randWindowPos() -> wx.Point:
	size = wx.GetDisplaySize().Get()
	return wx.Point( random.randrange( 0, size[ 0 ] ), random.randrange( 0, size[ 1 ] ) )


def randUnitBehavior() -> BehaviorBase.__class__:
	return random.choice(
		(
			BasicBehavior,
			FollowBehavior
		)
	)





