#!/usr/bin/python2.7
import thread
import time
import Queue
from scapy.all import *
import socket

sniffq = []

def customAction(packet):
#	return packet[0][1].src
	global sniffq
	#print sniffq
	source = packet.sprintf("{IP:%IP.src%}")
	#print "Source: " + source
	#print source + "	" + str(len(source))
	if source in sniffq:
		#print sniffq.index(source)
		return "niceeeeeeeeeeeeeeeeeeeeeeeeeeeee"
		#del sniffq[sniffq.index(source)]
		#return source
#	if source != socket.gethostbyname(socket.gethostname()) and source != "45.31.220.29":
#		return packet.sprintf("{IP:%IP.src%}")
	else: return "shit"

def sniffer(sniffq, i):
	try:
		print "starting sniffer"
		print sniff(prn=customAction)
	except Exception, s:
		print s
	return

f = open("ip.txt", "r")
thread.start_new_thread(sniffer, (sniffq, 1))
time.sleep(3)

for line in f:
	line = line.split("\r\n")[0]
	print line
	sniffq.append(line)
	pkt = IP(dst=line)/TCP(dport=[80], flags="S")
	send(pkt, verbose = False)
	time.sleep(0.3)
	print "Sent Ping to " + line 

while 1:
	pass	