#!/usr/bin/env python
#--*--coding:UTF-8--*--
import sys, socket
resultado=socket.getaddrinfo(sys.argv[1],None)
contador=0
for item in resultado:
      print "%2d: %s" % (contador,item[4])
      contador+=1

