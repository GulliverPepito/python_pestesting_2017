#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import sys, urllib2,re 
req=urllib2.Request(sys.argv[1])
req2=sys.argv[1].split(".")
req2.pop(0)
req3='.'.join(req2)
fd=urllib2.urlopen(req)
data=fd.readlines()
result=list(set(re.findall(r"http://(\w+)\."+req3,str(data))))
print "================================================="
print "       Resultado para el sitio "+req3 
print "=================================================\n\n"
i=0
for res in result:
	if res != 'www':
		print "sub dominio "+str(i)+" : "+res+"."+req3 
		i=i+1
print "\n================================================"
