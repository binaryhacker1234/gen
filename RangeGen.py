#!/usr/bin/python2.7
import threading
import Queue
import csv
import struct
import rangeByLoc
import os

class Gen(threading.Thread):
	def __init__(self, genq, outq, outqsize ):
		threading.Thread.__init__(self)
		self.active = 0
		self.genq = genq
		self.outq = outq
		self.outqsize = outqsize
	def run(self):
		self.active = 1
		range = self.genq.get()
		while self.active:
			start = int(range.split("-")[0])
			end = int(range.split("-")[1])
			i = start
			while i <= end:
				try:
					string = struct.unpack("BBBB", struct.pack(">L", i))
					#print str(string[0]) + "." + str(string[1]) + "." + str(string[2]) + "." + str(string[3])
					self.outq.put(str(string[0]) + "." + str(string[1]) + "." + str(string[2]) + "." + str(string[3]))
					i += 1
				except Queue.Full:
					while self.outq.size() > self.outqsize:
						pass
			range = self.genq.get()
		self.active = 0
		return	
	def stopgen(self):
		self.active = 0	



