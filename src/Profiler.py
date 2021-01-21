import json
from pathlib import Path
from time import time
from typing import Dict, List


class _Profiler:

	times: Dict[str, float]
	log: List[Dict[str, str]]

	def __init__(self):
		self.times = {}
		self.log = []

	def startState( self, state: str ):
		self.times[state] = time()

	def stopState( self, state: str ):
		self.log.append( { 'func': state, 'time': str( (time() - self.times[state] ) ) } )

	def save( self, loc: Path ):
		loc.parent.mkdir(exist_ok=True)
		loc.touch(exist_ok=True)
		loc.write_text(	json.dumps(self.log, indent=4) )


profiler = _Profiler()


def Restart():
	global profiler
	profiler.save( Path('./../profiling/latest.json') )
	profiler = _Profiler()