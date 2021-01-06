#!/usr/bin/env/python3

import webbrowser
#from selenium import webdriver
from time import sleep

url = input('What URL would you like to reload?')

refresh = 0

while refresh <= 10:
	print(refresh)
	webbrowser.open(url, new=0)
	sleep(2)
else:
	print('Refreshed 9999 times')
refresh += 1



