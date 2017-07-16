#!/usr/bin/env python
#--*--coding:UTF-8--*--

# Importamos los módulos
import socket
import errno

# Creación de 3 listas : para el conjunto de puertos a escanear, otra para guardar los puertos abiertos y una más para los puertos cerrados
ports=[21,22,25,53,80,139,443,1080,3128,8080,8081]
puertoabierto=[]
puertocerrado=[]

#  Introduzca la dirección IP a escanear por el usuario
print "Dirección IP a escanear?"
ip = raw_input()

i = 0
j = 0
while i < 10:
	# Creamos el socket
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	retourscan = s.connect_ex((ip,ports[i]))
	# Para la conexión exitosa
	if retourscan == 0:
		# cerramos la conexión
		s.shutdown(socket.SHUT_RDWR)
		# cerramos también el socket
		s.close()
		# Añadimos el puerto abierto a la lista
		puertoabierto.append(ports[i])
	# Para un error de conexión
	else:
		# Error de conexión - Puerto cerrado
		if errno.errorcode[retourscan]=="ECONNREFUSED":
			# añadimos el puerto cerrado a la lista
			puertocerrado.append(ports[i])
		# Error de conexión - Indicamos que el host no se encuentra
		else:
			print "Host no encontrado"
			j = 1
			# cerramos el boucle
			i = 10
	i = i + 1

#Si j = 1 cerramos el programa
if j==1:
	print "Cierre del programa."
# En caso contrario mostramos que todos los puertos están cerrados o los puertos abiertos y cerrados
else:
	if (len(puertoabierto) == 0):
		print "Todos los puertos están cerrados"
	else:
		print "Puertos cerrados:" , puertocerrado
		print "Puertos abiertos:" , puertoabierto
