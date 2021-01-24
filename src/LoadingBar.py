from typing import Tuple, Union

import wx

from BaseClasses import Tickable


class LoadingBar(wx.Frame, Tickable):

	initDrag: Union[ Tuple[ int, int ], None ] = None
	record: int = 0
	score: int = 0
	scoreTxt: wx.StaticText
	recordTxt: wx.StaticText
	limit: bool = True

	def __init__(self):
		super(LoadingBar, self).__init__(
			parent=None,
			size=wx.Size(400, 60),
			pos=wx.Point(200, 500),
			style=wx.BORDER_NONE | wx.FRAME_NO_TASKBAR
		)
		self.darkmode = False
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
		self.Show()
		self.Raise()

	def IsTouching( self, other: wx.Rect ):
		return self.GetScreenRect().Intersects( other )

	def IsScore( self, other: wx.Rect ):
		if other.GetPosition().Get()[ 1 ] > self.GetPosition().Get()[ 1 ]:
			return False
		return True

	def EndGame( self ):
		self.Show(False)
		wx.GetApp().playing = False
		wx.GetApp().units.clear()
		wx.GetApp().gameStage.ClearWindows()
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
			self.Show()
			wx.GetApp().playing = True
		else:
			wx.GetApp().Close()

	def AddScore( self, score: int ):
		if self.score + score <= 0:
			self.score = 0
		else:
			self.score += score

	def SetScore( self, score: int ):
		self.score = score

	def OnTick( self ):
		self.UpdateScore()
		self.UpdateRecord()

	def UpdateScore( self ):
		self.scoreTxt.SetLabel(f'score: {self.score}')

	def UpdateRecord( self ):
		self.recordTxt.SetLabel( f'record: {self.record}' )

	def UpdateColor( self ):
		if self.darkmode:
			self.SetBackgroundColour( wx.GetApp().GetColor( '#202120' ) )
			self.scoreTxt.SetForegroundColour( wx.GetApp().GetColor( '#F1EEDD' ) )
			self.recordTxt.SetForegroundColour( wx.GetApp().GetColor( '#F1EEDD' ) )
		else:
			self.SetBackgroundColour( wx.GetApp().GetColor( '#F1EEDD' ) )
			self.scoreTxt.SetForegroundColour( wx.GetApp().GetColor( '#202120' ) )
			self.recordTxt.SetForegroundColour( wx.GetApp().GetColor( '#202120' ) )
		self.Refresh()

	def OnKeyDown( self, evt: wx.KeyEvent ):
		if evt.GetUnicodeKey() == 68:
			self.darkmode = not self.darkmode
			self.UpdateColor()
		elif evt.GetUnicodeKey() == 76:
			self.limit = not self.limit
		elif evt.GetUnicodeKey() == 75:
			wx.GetApp().Close()

	def OnMouseClick( self, evt: wx.MouseEvent ):
		if evt.LeftIsDown():
			self.initDrag = evt.GetPosition().Get()
		else:
			self.initDrag = None

	def OnMouseMove( self, evt: wx.MouseEvent ):
		if evt.Dragging() and ( self.initDrag is not None ):
			nextX = self.GetPosition().Get()[ 0 ] + ( evt.GetX() - self.initDrag[ 0 ] )
			nextY = self.GetPosition().Get()[ 1 ] + ( evt.GetY() - self.initDrag[ 1 ] )
			if ( nextY < 200 ) and self.limit:
				return
			nextRect = wx.Rect( nextX, nextY, 400, 60 )
			for window in wx.GetApp().windows:
				if window.GetRect().Intersects( nextRect ):
					window.OnCollide( self.GetRect() )
					return
			self.Move( wx.Point(nextX, nextY) )
