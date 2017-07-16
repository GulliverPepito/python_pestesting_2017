#!/usr/bin/env python
#--*-- coding:UTF-8 --*--
import socket,sys
host=sys.argv[1]
textport=sys.argv[2]
archivo=sys.argv[3]
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,e:
	print "error en la creación del socket: %s" %e
	sys.exit(1)
try:
	port=int(textport)
except ValueError:
	try:
		port=socket.getservbyname(host,'tcp')
	except socket.error,e:
		print "no se encuentra el puerto %s" %e
		sys.exit(1)
try:
	s.connect((host,port))
except socket.gaierror, e:
	print "error de dirección de conexión al servidor:%s" %e
	sys.exit(1)
except socket.error, e:
	print "error de conexión: %s" %e
	sys.exit(1)
try:
	s.sendall("GET %s HTTP/1.0\r\n\r\n" % archivo)
except socket.error, e:
	print "error de envío de datos: %s " %e
	sys.exit(1)
while 1:
	try:
		buf=s.recv(2048)
	except socket.error, e:
		print "error de recepción de datos: %s" %e
		sys.exit(1)
	if not len(buf):
		break
	print buf



