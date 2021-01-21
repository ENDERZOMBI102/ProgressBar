from typing import NamedTuple, Tuple, Union, List
import math

import wx


class Point( wx.Point ):
	"""
		Point()
		Point(x, y)
		Point(pt)
		Point(pt)
	"""

	IM: NamedTuple = property( lambda self: object(), lambda self, v: None, lambda self: None )  # default
	"""
		Returns an immutable representation of the ``wx.Point2D`` object, based on ``namedtuple``.
		
		This new object is hashable and can be used as a dictionary key,
		be added to sets, etc.  It can be converted back into a real ``wx.Point2D``
		with a simple statement like this: ``obj = wx.Point2D(imObj)``.
	"""

	VectorAngle: int = property( lambda self: object(), lambda self, v: None, lambda self: None )
	""" GetVectorAngle() -> int """

	VectorLength: int = property( lambda self: object(), lambda self, v: None, lambda self: None )
	""" GetVectorLength() -> int """

	x: int = None
	y: int = None

	def __init__( self, *args: Union[
			int,
			Tuple[int, int],
			List[int],
			NamedTuple,
			wx.Point
	], **kwargs ):
		if len( args ) > 0:
			if len( args ) == 2 and isinstance(args[0], int ) and isinstance(args[1], int):
				x, y = args[0], args[1]
			elif len( args ) == 1 and ( isinstance(args[0], tuple) or isinstance(args[0], NamedTuple) or isinstance(args[0], list) ):
				x, y = args[0][0], args[0][1]
			elif len( args ) == 1 and isinstance(args[0], wx.Point):
				x, y = args[0].Get()
			else:
				raise ValueError(f'Unknown parameters given! {args}')
		elif len( kwargs ) > 0:
			if 'x' in kwargs.keys() and 'y' in kwargs.keys():
				x, y = kwargs['x'], kwargs['y']
			elif 'pt' in kwargs.keys():
				x, y = kwargs['pt'].Get()
		else:
			x, y = 0, 0
		super().__init__( int(x), int(y) )
		self.x = x
		self.y = y

	def Get( self ) -> Tuple[int, int]:
		"""
			Get() -> (x,y)

			Return the x and y properties as a tuple.
		"""
		return self.x, self.y

	def GetDistance( self, pt: 'Point' ) -> float:
		""" GetDistance(pt) -> float """
		disH = ( self.x - pt.x ) ** 2
		disV = ( self.y - pt.y ) ** 2
		return math.sqrt( disH + disV )

	def GetDistanceSquare( self, pt ) -> int:
		""" GetDistanceSquare(pt) -> int """
		return int( self.GetDistance() )

	def GetImmutable( self ) -> NamedTuple:
		"""
			Returns an immutable representation of the ``wxGeometry.Point`` object, based on ``namedtuple``.

			This new object is hashable and can be used as a dictionary key,
			be added to sets, etc.  It can be converted back into a real ``wxGeometry.Point``
			with a simple statement like this: ``obj = wxGeometry.Point(imObj)``.
		"""
		pass

	def __eq__( self, pt: wx.Point ) -> bool:
		""" Return self==value. """
		return self.Get() == pt.Get()

	def __ge__( self, pt: wx.Point ) -> bool:
		""" Return self>=value. """
		pass

	def __neg__( self, pt: wx.Point ) -> 'Point':
		""" -self """
		return Point( -self.x, -self.y )

	def __ne__( self, pt: wx.Point ) -> bool:
		""" Return self!=value. """
		return not self.__eq__(pt)

	def __gt__( self, pt: wx.Point ) -> bool:
		""" Return self>value. """
		pass

	def __le__( self, pt: wx.Point ) -> bool:
		""" Return self<=value. """
		pass

	def __lt__( self, pt: wx.Point ) -> bool:
		""" Return self<value. """
		pass

	def __iadd__( self, pt: wx.Point ) -> 'Point':
		""" Return self+=value. """
		self.x = self.x + pt.x
		self.y = self.y + pt.y
		return self

	def __imul__( self, pt: wx.Point ) -> 'Point':
		""" Return self*=value. """
		self.x = self.x * pt.x
		self.y = self.y * pt.y
		return self

	def __isub__( self, pt: wx.Point ) -> 'Point':
		""" Return self-=value. """
		self.x = self.x - pt.x
		self.y = self.y - pt.y
		return self

	def __itruediv__( self, pt: wx.Point ) -> 'Point':
		""" Return self/=value. """
		self.x = int( self.x / pt.x )
		self.y = int( self.y / pt.y )
		return self

	def __add__( self, pt: wx.Point ) -> 'Point':
		""" Return self+=value. """
		return Point( int( self.x + pt.x ), int( self.y + pt.y ) )

	def __mul__( self, pt: wx.Point ) -> 'Point':
		""" Return self*=value. """
		return Point( int( self.x * pt.x ), int( self.y * pt.y ) )

	def __sub__( self, pt: wx.Point ) -> 'Point':
		""" Return self-=value. """
		return Point( int( self.x - pt.x ), int( self.y - pt.y ) )

	def __truediv__( self, pt: wx.Point ) -> 'Point':
		""" Return self/=value. """
		return Point( int( self.x / pt.x ), int( self.y / pt.y ) )
