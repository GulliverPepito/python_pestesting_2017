#!/usr/bin/env python
# --*-- coding: UTF-8 --*--
import sys, socket
result=socket.getaddrinfo("www.google.es",None,0,socket.SOCK_STREAM)
print result
print result[0][4]
contador=0
for item in result:
	print "%-2d: %s" % (contador,item[4])
	contador+=1

