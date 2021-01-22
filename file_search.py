#!/usr/bin/env python3

import os
import fnmatch

for root, dirs, files in os.walk('test/'): # change path
   for file in files:
       with open(os.path.join(root, file), "r") as findit:
            f = findit.read()
            if "" in f: # change string to search for
                  print("String found in", file)
