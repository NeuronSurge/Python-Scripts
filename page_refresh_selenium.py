#!/usr/bin/env python3

from selenium import webdriver
from time import sleep

refresh = 0

while True:
	driver = webdriver.Firefox()
	webpage = input("Enter Your URL: ")
	driver.get(webpage)
	time.sleep(5)
	driver.refresh()
	refresh += 1

	if refresh == 10:
		break