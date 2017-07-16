#!/usr/bin/env python
#--*--coding:UTF-8--*--

import sys,DNS,cap2_exo16,re

def getreverse(query):
	if re.search('^\d+\.\d+\.\d+\.\d+$',query):
		octets=query.split('.')
		octet.reverse()
		return '.'.join(octets)+'.IN-ADDR.ARPA'
	return None

def formatline(index, typename, descr,data):
	retval="%-2s %-5s"%(index,typename)
	data=data.replace("\n", "\n      ")
	if descr != None and len(descr):
		retval += " %-12s"%(descr + ":")
	return retval + " "+data

DNS.DiscoverNameServers()
queries=[(sys.argv[1], DNS.Type.ANY)]
print queries
donequeries=[]
descriptions={"A":"dirección IP","TXT":"Data","PTR":"nombre de host","CNAME":"Alias para ","NS":"Servidor de nombres"}
while len(queries):
    (query,qtype)=queries.pop(0)
    print query 
    print qtype
    if query in donequeries:
        continue
    donequeries.append(query)
    print "-"*77
    print "Resultados para %s(lookup type %s)"%(query,DNS.Type.typestr(qtype))
    print 
    rev=getreverse(query)
    if rev:
        print "Dirección Ip recuperada, arranque de la búsqueda inversa (reverse lookup) con",rev
        query=rev
    answers=cap2_exo16.nslookup(query,qtype,verbose=0)
    if not len(answers):
        print "no encontrado"

	count =0
	for answer in answers:
		count +=1
		if answer['typename'] == 'MX':
			print formatline(count,answer['typename'],'Servidor Mail',"%s, prioridad %d"%(answer['data'][1],answer['data'][0]))
			queries.append((answer['data'][1],DNS.Type.A))
		elif answer['typename']=="SOA":
			data="\n"+"\n".join([str(x) for x in answer['data']])
			print formatline(count,'SOA','Inicio de Autoridad',data)
		elif answer['typename'] in descriptions:
			print formatline(count,answer['typename'],descriptions[answer['typename']],answer['data'])
		else:
			 print formatline(count,answer['typename'],None, str(answer['data']))
		if answer['typename'] in ['CNAME','PTR']:
			queries.append((answer['data'],DNS.Type.ANY))
		
		if answer['typename'] == 'NS':
			queries.append((answer['data'],DNS.Type.A))
