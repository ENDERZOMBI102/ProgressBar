from enum import Enum
from typing import Dict

import wx


class MouseButton( Enum ):
	RIGHT = 0
	MIDDLE = 1
	LEFT = 2


IGNORED_MOUSE_BTN_LIST = (
	wx.MOUSE_BTN_NONE,
	wx.MOUSE_BTN_ANY,
	wx.MOUSE_BTN_MAX,
	wx.MOUSE_BTN_AUX1,
	wx.MOUSE_BTN_AUX2
)


MOUSE_BTN_LOOKUP: Dict[int, MouseButton] = {
	wx.MOUSE_BTN_RIGHT: MouseButton.RIGHT,
	wx.MOUSE_BTN_MIDDLE: MouseButton.MIDDLE,
	wx.MOUSE_BTN_LEFT: MouseButton.LEFT
}


def IsTouching( rect0: wx.Rect, rect1: wx.Rect ) -> bool:
	return rect0.GetLeft() == rect1.GetLeft() or \
		rect0.GetRight() == rect1.GetRight() or \
		rect0.GetTop() == rect1.GetTop() or \
		rect0.GetBottom() == rect1.GetBottom()