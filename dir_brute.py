#!/usr/bin/env/ python3

import sys
import socket
import requests

rhost = sys.argv[1]
wordlist = sys.argv[2]

print("[*] Checking RHOST....)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	status = s.connect_ex((rhost, #port))
	s.close()
	if status == 0:
		print("Check Complete, Success!!")
		pass
	else:
		print("Check Failed!!")
		print("Cannot reach RHOST %s" %rhost)
		sys.exit(1)
except socket.error:
	print("Connection Failed!!")
	print("Cannot reach RHOST %s" %rhost)
	sys.exit(1)

print("[*] Accessing Wordlist....")
try:
	with open(wordlist) as file:
		to_check = file.read().strip().split('\n')
	print("Check Complete!!")
	print("Paths to check: %s" %(str(len(to_check)))
except IOerror:
	print("Check Failed!!")
	print("Failed to read specified file!!")
	sys.exit(1)

def checkpath(path):
	try:
		response = requests.get('http://' + rhost + '/' + path).status_code
	except Exception:
		print("[!] ERROR: An unexpected error occured!!")
		sys.exit(1)
	if response == 200:
		print("Valid path FOUND!!: %s" %(path)
		print("Beginning Scan...")
		for i in range(len(to_check)):
			checkpath(to_check[i])
		print("Scan Complete!!")
	except KeyboardInterrupt:
		print("[!] ERROR: User Interrupted Scan")
		sys.exit(1)
