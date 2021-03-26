#!/usr/bin/env python3

import binascii


flag_enc = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

flag_ord = [o for o in bytes.fromhex(flag_enc)]

for key in range(256):
    flag_de_xored_ord = ''.join(chr(o ^ key) for o in flag_ord) 
    if flag_de_xored_ord.isprintable():
        print(flag_de_xored_ord)
