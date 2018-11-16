#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
"""
Url encode
    Exec: python urlEncode.py urlToEncode [2]
    [2]: Use "2" parameter to double encode the url, if you dont specify this parameter the programm will use simple encodage
"""
urlEncoded=""
lvl=1
if len(sys.arv) == 1:

if(sys.argv[1] == 2):lvl=2
for c in sys.argv[1]:
    if c == ".":
        if lvl == 2: c="%2E"
        else: c= "%252E"
    elif c == "/":
        if lvl == 2: c="%2F"
        else:c="%252F"
    urlEncoded+=c
print(urlEncoded)
