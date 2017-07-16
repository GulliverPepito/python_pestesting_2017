#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket

print 'creación de socket ...'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'socket creado'
print "conexión al host remoto"
s.connect(('localhost',80))
print 'conexión efectuada'
s.send( 'GET /index.html HTML/1.1\r\n\r\n')
while 1:
	data=s.recv(128)
	print data
	if data== "":
		break
print 'antes de cerrar'
s.close()
