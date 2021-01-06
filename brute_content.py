#!/usr/bin/env python3

import urllib
import urllib2
import threading
import Queue

threads = 50
target_url = "" #insert target url
wordlist_file = "" #insert path to WL
resume = None
user_agent = "" #insert user agent

def build_wordlist(wordlist_file):
	fd = open(wordlist_file, "rb")
	raw_words = fd.readlines()
	fd.close()

	found_resume = False
	words = Queue.Queue()

	for word in raw_words:
		word = word.rstrip()

		if resume is not None:

			if found_resume:
				words.put(word)
			else:
				if word == resume:
					found_resume = target_url
					print("Resuming wordlist from: %s" %resume)
		else:
			words.put(word)

	return words
