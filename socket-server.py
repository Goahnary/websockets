#!/usr/bin/python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5823
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'connection address: ', addr
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print "received data:", data
	conn.send(data) #send the data back
conn.close()

