#!/usr/bin/python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5822
BUFFER_SIZE = 128
MESSAGE = ""

print "Welcome to my python network client!"

while(MESSAGE != "exit"):
	MESSAGE = raw_input("Enter some text: ")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE)
	data = s.recv(BUFFER_SIZE)
	s.close()
	print "reply: ", data

print "Exiting client program!"
