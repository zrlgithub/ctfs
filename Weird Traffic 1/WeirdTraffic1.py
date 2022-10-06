#!/usr/bin/env python

from scapy.all import *
from pwn import *
import os
import subprocess
import codecs

packets = rdpcap('Chall_1.pcapng')
str=""
with open("aoutSPI.txt","w") as fout:
	subprocess.run(["tshark","-r",os.path.join(os.path.dirname(os.path.realpath("WeirdTraffic1.py")),"Chall_1.pcapng"),"-V","-J esp.spi"],stdout=fout,check=True)

with open("grepSPI.txt","w") as fOut:
	subprocess.run(["grep","ESP SPI:",fout.name],stdout=fOut)

f = open(fOut.name,"r")
for line in f.readlines():
    if not "ESP SPI:" in line:
       continue
    try:
       spi = line.split("ESP SPI:")[1].split(" ")[1]
      # print(line.split("ESP SPI:")[1].split(" ")[1][2:])   
       str+=hex(int(spi,16))[2:]
      # print(hex(int(spi,16))[2:])
      # print(str(codecs.decode(spi,"hex"),'utf-8'))
    except IndexError:
        print

print(str)
#print(bytes.fromhex(str).decode("ASCII"))
#sa = SecurityAssociation(ESP, spi=0x00000033, crypt_algo='AES-CBC', crypt_key=str)
#res = sa.decrypt(packets[0])
#res.show()
