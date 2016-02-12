#!/usr/bin/python

import socket

TCP_IP = '161.6.10.102'
TCP_PORT = 5005
BUFFER_SIZE = 20
MESSAGE = "Hello, world!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "reply: ", data
