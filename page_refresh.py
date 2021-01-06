#!/usr/bin/env/python3

import webbrowser
#from selenium import webdriver
from time import sleep

url = input('What URL would you like to reload?') #insert reload incl http://

refresh = 0

while True:
	print(refresh)
	webbrowser.open(url, new=0)
	sleep(2)
	refresh += 1
	
	if refresh == #insert number or reloads
	break


