#!/usr/bin/env python3

from pwn import *

r = remote(#IP Addr, #PORT)

r.recvline_contains(#Insert Welcome msg from server)
while True:
	s = r.recvline(False)
	print(s)
	if s.endswith('='):
		answer = str(eval(s[:-1]))
		print(answer)
		r.sendline(answer)