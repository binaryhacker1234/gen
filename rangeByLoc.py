import Queue
import csv
import os
def grab(q, loc):
	print os.getcwd()
	f = open("IPv4.CSV", "r")
	readCSV = csv.reader(f)
	
	counter = 0
	for row in readCSV:
		if len(set(loc).intersection(row)) == len(loc):
			#print row
			q.put(row[0] + "-" + row[1])