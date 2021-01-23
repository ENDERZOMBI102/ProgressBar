import random
from time import time

import wx
from PIL import ImageGrab

from Score import ScoreData
from units.ErrorUnit import ErrorUnit
from units.FillUnit import FillUnit
from units.JollyUnit import JollyUnit
from units.MalusUnit import MalusUnit
from units.MultiUnit import MultiUnit
from units.NormalUnit import NormalUnit
from units.NullUnit import NullUnit
from units.WrongUnit import WrongUnit
from windows.WindowBase import WindowBase


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
		img = ImageGrab.grab( bbox=(disp.x, disp.y, disp.width, disp.height) )
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
		self.app.windows.Clear()

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
				WindowBase(
					pos=randWindowPos()
				)
			)

	def SpawnUnit( self ):
		n = random.randrange( 100 )
		if n > 90:
			self.app.units.append(
				ErrorUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 )
				)
			)
		elif n > 70:
			self.app.units.append(
				WrongUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 )
				)
			)
		elif n > 40:
			self.app.units.append(
				NormalUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 )
				)
			)
		elif n > 33:
			self.app.units.append(
				MalusUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 )
				)
			)
		elif n > 26:
			self.app.units.append(
				NullUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 )
				)
			)
		elif n > 20:
			self.app.units.append(
				MultiUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					scoreMultiplier=random.randrange( 1, 3 )
				)
			)
		elif n > 13:
			self.app.units.append(
				JollyUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 ),
					initialState=random.randrange( 0, 5 )
				)
			)
		elif n > 9:
			self.app.units.append(
				FillUnit(
					pos=randUnitPos(),
					speed=random.randrange( 2, 10 )
				)
			)


def randUnitPos() -> wx.Point:
	size = wx.GetDisplaySize().Get()
	return wx.Point( random.randrange( 0, size[ 0 ] ), -40 )


def randWindowPos() -> wx.Point:
	size = wx.GetDisplaySize().Get()
	return wx.Point( random.randrange( 0, size[ 0 ] ), random.randrange( 0, size[ 1 ] ) )





