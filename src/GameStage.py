import wx
from PIL import ImageGrab

from Score import ScoreData


class GameStage(wx.Frame):

	screen: wx.Bitmap
	dc: wx.WindowDC
	score: ScoreData

	def __init__(self):
		super(GameStage, self).__init__(
			None
		)
		self.initScreen()
		self.dc = wx.WindowDC(self)

		self.ShowFullScreen(True)
		self.Raise()

		self.Bind(wx.EVT_SET_FOCUS, lambda evt: wx.GetApp().loadBar.Raise() if wx.GetApp().playing else print(end='') )

	def initScreen( self ):
		img = ImageGrab.grab()
		wx_img = wx.Image( img.width, img.height, img.convert( 'RGB' ).tobytes() )
		if img.mode[ -1 ] == 'A':
			alpha = img.getchannel( "A" ).tobytes()
			wx_img.InitAlpha()
			for i in range( wx_img.GetWidth() ):
				for j in range( wx_img.GetHeight() ):
					wx_img.SetAlpha( i, j, alpha[ i + j * img.width ] )
		self.screen = wx_img.ConvertToBitmap()

	def clear( self ):
		self.dc.DrawBitmap(self.screen, 0, 0)

