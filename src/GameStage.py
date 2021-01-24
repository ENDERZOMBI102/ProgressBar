import random
from time import time

import wx
from PIL import ImageGrab

from Score import ScoreData
from unit.ErrorUnit import ErrorUnit
from unit.FillUnit import FillUnit
from unit.JollyUnit import JollyUnit
from unit.MalusUnit import MalusUnit
from unit.MultiUnit import MultiUnit
from unit.NormalUnit import NormalUnit
from unit.NullUnit import NullUnit
from unit.WrongUnit import WrongUnit
from distraction.DistractionBase import DistractionBase
from unit.behavior.BasicBehavior import BasicBehavior
from unit.behavior.BehaviorBase import BehaviorBase


class GameStage(wx.Frame):

	screen: wx.Bitmap
	dc: wx.WindowDC
	score: ScoreData
	spawnUnitTimer = time()
	app: 'ProgressBar'
	spawnDistractionTimer = time()
	diffMultiplier: float = 1.0

	def __init__(self):
		super(GameStage, self).__init__(
			None
		)
		self.InitScreen()
		self.dc = wx.WindowDC(self)

		self.app = wx.GetApp()

		self.ShowFullScreen(True)
		self.Raise()

		self.Bind(wx.EVT_SET_FOCUS, lambda evt: wx.GetApp().loadBar.Raise() if wx.GetApp().playing else print(end='') )

	def InitScreen( self ):
		disp: wx.Rect = wx.Display( wx.Display.GetFromWindow(self) ).GetGeometry()
		img = ImageGrab.grab( bbox=( disp.GetX(), disp.GetY(), disp.GetWidth(), disp.GetHeight() ) )
		wx_img = wx.Image( img.width, img.height, img.convert( 'RGB' ).tobytes() )
		if img.mode[ -1 ] == 'A':
			alpha = img.getchannel( "A" ).tobytes()
			wx_img.InitAlpha()
			for x in range( wx_img.GetWidth() ):
				for y in range( wx_img.GetHeight() ):
					wx_img.SetAlpha( x, y, alpha[ x + y * img.width ] )
		self.screen = wx_img.ConvertToBitmap()

	def Clear( self ):
		self.dc.DrawBitmap(self.screen, 0, 0)

	def ClearWindows( self ):
		for window in self.app.windows:
			window.Destroy()
		self.app.windows.clear()

	def Tick( self ):
		# spawn units
		if time() - self.spawnUnitTimer > (random.randrange( 1, 3 ) * random.randrange( 1, 3 )) * self.diffMultiplier:
			if len( self.app.units ) < 30:
				self.spawnUnitTimer = time()
				self.SpawnUnit()
		# spawn distractions
		if time() - self.spawnDistractionTimer > (random.randrange( 1, 3 ) * random.randrange( 1, 3 )) * self.diffMultiplier:
			if len( self.app.windows ) < 10:
				self.spawnDistractionTimer = time()
				self.SpawnDistraction()

	def SpawnDistraction( self ):
		n = random.randrange( 100 )
		if n < 10:
			self.app.windows.append(
				DistractionBase(
					pos=randWindowPos()
				)
			)

	def SpawnUnit( self ):
		n = random.randrange( 100 )
		if n > 90:
			self.app.units.append(
				ErrorUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)
		elif n > 70:
			self.app.units.append(
				WrongUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)
		elif n > 40:
			self.app.units.append(
				NormalUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)
		elif n > 33:
			self.app.units.append(
				MalusUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)
		elif n > 26:
			self.app.units.append(
				NullUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior()
				)
			)
		elif n > 20:
			self.app.units.append(
				MultiUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior(),
					scoreMultiplier=random.randrange( 1, 3 )
				)
			)
		elif n > 13:
			self.app.units.append(
				JollyUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					behavior=randUnitBehavior(),
					initialState=random.randrange( 0, 5 )
				)
			)
		elif n > 9:
			self.app.units.append(
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

		)
	)





