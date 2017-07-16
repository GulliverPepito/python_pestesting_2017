#!/usr/bin/env python
#coding:utf-8

import socket, sys
from OpenSSL import SSL

cafile, host=sys.argv[1:]

def printx509(x509):
	fields={'country_name':'Country',
		'SP':'State/Province',
		'L':'Locality',
		'O':'Organization',
		'OU':'Organiztion Unit',
		'CN':'Common Name',
		'email':'E-mail',}
	for field, desc in fields.items():
		try:
			print "%30s: %s"%(desc,getattr(x509,field))
		except:
			pass
cnverified=0
def verify(connection, certificate,ernum,depth, ok):
	global cnverified
	subject=certificate.get_subject()
	issuer=certificate.get_issuer()
	print "Certificado de:"
	printx509(subject)
	print "\nEmitido por:"
	if not ok:
		print "No puedo verificar el certificado"
		return 0
	if subject.CN==None or subject.CN.lower() != host.lower():
		print "Conectado a %s, pero con el certificado de %s"%(host,subject.CN)
	else:
		cnverified=1
	if depth ==0 and not cnverified:
		print "No puedo verificar el nombre del servidor"
		return 0
	print "-"*70
	return 1

ctx=SSL.Context(SSL.SSLv23_METHOD)
ctx.load_verify_locations(cafile)
ctx.set_verify(SSL.VERIFY_PEER|SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verify)
print "creación del socket..."
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Hecho"
ssl=SSL.Connection(ctx,s)
print "Establecimiento de ssl..."
ssl.connect((host,443))
print "Hecho"
print "Solicitud del documento..."
ssl.sendall("GET / HTTP/1.0\r\n\r\n")
print "Hecho"
while 1:
	try:
		buf=ssl.recv(4096)
	except SSL.ZeroReturnError:
		break
	print buf
ssl.close()
