# coding: utf8
# author: xiaonanln

import sys
import time
import traceback

_watchdogs = {}
_maxWatchdogID = 0


class Watchdog(object):
	def __init__(self, timeout, callback):
		self.timeout = timeout
		self.callback = callback
		self.timeoutTS = time.time() + timeout

	def reset(self):
		self.timeoutTS = time.time() + self.timeout

	def check(self):
		if time.time() >= self.timeoutTS:
			self.reset()
			self.callback()

def setup(name, timeout, callback):
	"""Create a watchdog with timeout and callback
	:arg: timeout timeout of watchdog
	:arg: callback called when watchdog fail
	:return: watchdog ID
	"""
	_watchdogs[name] = Watchdog(timeout, callback)


def cancel(name):
	if name in _watchdogs:
		del _watchdogs[name]


def reset(name):
	"""Reset a watchdog so that it won't fail
	:arg id watchdog ID returned by create function
	"""
	assert name in _watchdogs, ('watchdog %s not found' % name)
	_watchdogs[name].reset()


def check():
	"""
	check all watchdogs and make them fail when timeout
	"""
	for name, watchdog in _watchdogs.iteritems():
		try:
			watchdog.check()
		except:
			print >>sys.stderr, 'Watchdog %s check failed: ' % name
			traceback.print_exc()
			watchdog.reset()
