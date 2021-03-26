#!/usr/bin/env python3

word = "label"; key = 13; flag = ''

for i,j in enumerate(word):
    flag += chr(13 ^ ord(j))

print('crypto{'+flag+'}')
