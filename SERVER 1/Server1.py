#!/usr/bin/env python

from scapy.all import *
from pwn import *

import os
from itertools import cycle
import base64

def _xor(ciphertext,key):
	ct = ciphertext
	len_key = len(key)
	encoded = []
	
	for i in range(0,len(ct)):
	    encoded.append(ct[i]^key[i%len_key])
	return bytes(encoded)

key=""

g = open("ofuscated_keys","r").read()
f = open("k.log","w");
for i in range(0,255):
    kk = _xor(base64.b64decode(g),i.to_bytes(1,byteorder='big'))
    k=kk.hex()
    f.write("CLIENT_RANDOM")
    f.write(" ")
    f.write(k[:64])
    f.write(" ")
    f.write(k[-96:])
    f.write("\n")
