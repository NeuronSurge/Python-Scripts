#!/usr/bin/env python3

import requests
import re
from time import sleep

url = input('Enter the URL: ') # Enter URL to refresh

#p = re.compile('') # Enter regex to search for

refresh = 0

while True: # Can change to num of refreshes needed
	print('Refreshing...' + str(refresh))
	r = requests.get(url=url)
	sleep(0.5) # Time to wait between page refresh
	#if (p.match(r.text)): continue # Only needed if searching with regex
	refresh += 1

	if refresh == 5:
		print(r.text)
		break