from typing import Tuple, Union

import wx


class Bar(wx.Frame):

	initDrag: Union[ Tuple[ int, int ], None ] = None
	score: int = 0
	record: int = 0
	scoreTxt: wx.StaticText
	recordTxt: wx.StaticText

	def __init__(self):
		super(Bar, self).__init__(
			parent=None,
			size=wx.Size(400, 60),
			pos=wx.Point(200, 500),
			style=wx.BORDER_NONE | wx.FRAME_NO_TASKBAR
		)
		self.darkmode = True
		self.scoreTxt = wx.StaticText(
			parent=self,
			pos=wx.Point(20, 10),
			label='score: 0'
		)
		self.recordTxt = wx.StaticText(
			parent=self,
			pos=wx.Point( 20, 30 ),
			label='record: 0'
		)
		self.UpdateColor()
		# bind events
		self.Bind( wx.EVT_LEFT_DOWN, self.OnMouseClick )
		self.Bind( wx.EVT_LEFT_UP, self.OnMouseClick )
		self.Bind( wx.EVT_MOTION, self.OnMouseMove )
		self.Bind( wx.EVT_KEY_DOWN, self.OnKeyDown )

	def UpdateScore( self ):
		self.scoreTxt.SetLabel(f'score: {self.score}')

	def IsTouching( self, other: wx.Frame ):
		return self.GetScreenRect().Intersects( other.GetScreenRect() )

	def IsScore( self, other: wx.Frame ):
		if other.GetPosition().Get()[ 1 ] > self.GetPosition().Get()[ 1 ]:
			return False
		return True

	def EndGame( self ):
		self.SetPosition( wx.Point(0, wx.GetDisplaySize().Get()[1] + 200) )
		wx.GetApp().playing = False
		wx.GetApp().KillUnits()
		newRecord = self.score > self.record
		msg = f'Final Score: {self.score}\nRecord: {self.record}'
		if newRecord:
			msg += f'\nNew Record! you got {self.score - self.record} more points than last time!'
			self.record = self.score
		msg += '\n\nPress "yes" to play again'
		diag = wx.GenericMessageDialog(
			parent=self,
			message=msg,
			caption='Game over man! its Game over!',
			style=wx.YES_NO | wx.CENTRE
		)
		choice = diag.ShowModal()
		if choice == wx.ID_YES:
			self.score = 0
			self.UpdateScore()
			self.recordTxt.SetLabel(f'record: {self.record}')
			self.CenterOnScreen()
			wx.GetApp().playing = True
		else:
			self.Destroy()

	def UpdateRecord( self ):
		self.scoreTxt.SetLabel( f'record: {self.score}' )

	def UpdateColor( self ):
		if self.darkmode:
			self.SetBackgroundColour( wx.Colour( '#202120' ) )
			self.scoreTxt.SetForegroundColour( wx.Colour( '#F1EEDD' ) )
			self.recordTxt.SetForegroundColour( wx.Colour( '#F1EEDD' ) )
		else:
			self.SetBackgroundColour( wx.Colour( '#F1EEDD' ) )
			self.scoreTxt.SetForegroundColour( wx.Colour( '#202120' ) )
			self.recordTxt.SetForegroundColour( wx.Colour( '#202120' ) )

	def OnKeyDown( self, evt: wx.KeyEvent ):
		if evt.GetUnicodeKey() == 'd':
			self.darkmode = not self.darkmode
			self.UpdateColor()

	def OnMouseClick( self, evt: wx.MouseEvent ):
		if evt.LeftIsDown():
			self.initDrag = evt.GetPosition().Get()
		else:
			self.initDrag = None

	def OnMouseMove( self, evt: wx.MouseEvent ):
		if evt.Dragging() and (self.initDrag is not None):
			# if self.GetPosition().Get()[ 1 ] + ( evt.GetY() - self.initDrag[ 1 ] ) < 200:
			# 	return
			self.SetPosition(
				wx.Point(
					self.GetPosition().Get()[ 0 ] + ( evt.GetX() - self.initDrag[ 0 ] ),
					self.GetPosition().Get()[ 1 ] + ( evt.GetY() - self.initDrag[ 1 ] )
				)
			)




