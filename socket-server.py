#!/usr/bin/python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5822
BUFFER_SIZE = 128
data = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))

while data != "EXIT":
	s.listen(1)
	conn, addr = s.accept()
	print 'connection address: ', addr
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	data = data.upper()
	print "received data:", data
	conn.send(data) #send the data back

conn.close()

