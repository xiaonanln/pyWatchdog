# coding: utf8

import unittest
import time
import pyWatchdog


class TestPyWatchdog(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestPyWatchdog, self).__init__(*args, **kwargs)
		self.watchdogFailed = False

	def setUp(self):
		self.watchdogFailed = False

	def tearDown(self):
		pass

	def onWatchdogFail(self):
		print 'onWatchdogFail!!!'
		self.watchdogFailed = True

	def testSetupWatchdog(self):
		pyWatchdog.setup('watchdog', 0.1, self.onWatchdogFail)

	def testWatchdogTimeout(self):
		pyWatchdog.setup('watchdog', 0.1, self.onWatchdogFail)
		self.assertFalse(self.watchdogFailed)
		self.loopForAWhile(0.11)
		self.assertTrue(self.watchdogFailed)

	def testWatchdogReset(self):
		pyWatchdog.setup('watchdog', 0.1, self.onWatchdogFail)
		self.assertFalse(self.watchdogFailed)
		self.loopForAWhile(0.05)
		self.assertFalse(self.watchdogFailed)
		pyWatchdog.reset('watchdog')
		self.loopForAWhile(0.05)
		self.assertFalse(self.watchdogFailed)

	def testWatchdogCancel(self):
		pyWatchdog.setup('watchdog', 0.1, self.onWatchdogFail)
		self.assertFalse(self.watchdogFailed)
		self.loopForAWhile(0.05)
		self.assertFalse(self.watchdogFailed)
		pyWatchdog.cancel('watchdog')
		self.loopForAWhile(0.05)
		self.assertFalse(self.watchdogFailed)

	def loopForAWhile(self, duration, tickInterval=0.001):
		endTime = time.time() + duration
		while time.time() < endTime:
			time.sleep(tickInterval)
			pyWatchdog.loop()

if __name__ == '__main__':
	unittest.main()

