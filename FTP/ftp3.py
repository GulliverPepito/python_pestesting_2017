#!/usr/bin/env python

# --*-- coding: UTF-8 --*--

from ftplib import FTP

f=FTP('ftp.kernel.org')

f.login()

f.cwd('/pub/linux/kernel')

entre=f.nlst()

entre.sort()

print "%d entradas:"%len(entrada)

for item in entrada:

	print item

f.quit()

