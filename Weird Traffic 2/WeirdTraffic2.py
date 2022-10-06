#!/usr/bin/env python3

from scapy.all import *
from pwn import *

import base64
import os

g = open("payload_all.txt","r").read()
packets = rdpcap('Chall_2.pcapng')

sourceIps = []
i=0
##for p,packet in enumerate(packets):
#    if p == 0:	
#       sourceIps.insert(i,packet[IP].src)
#       print(packet[IP].src)
#       i=i+1
ssl_packets = []
client_ip_addr = None
server_ip_addr = None
for i, packet in enumerate(packets):
    if packet.haslayer(IP) == 1:
            client_ip_addr = packet[IP].src
   
strr=[]

with open("aoutESP.txt","w") as fout:
	subprocess.run(["tshark","-r",os.path.join(os.path.dirname(os.path.realpath("WeirdTraffic1.py")),"Chall_2.pcapng"),"-V","-J esp"],stdout=fout,check=True)

with open("grepESP.txt","w") as fOut:
	subprocess.run(["grep","Source Address:",fout.name],stdout=fOut)
flag=""	
f = open(fOut.name,"r")
for line in f.readlines():
    if not "Source Address:" in line:
       continue
    try:
      if not "10." in line:
          if not "192.168" in line:
             spi = line.split("Source Address:")[1].split(" ")[1]
             spi2 = spi.split('.')
             strr.append(spi2[-1].strip())
             asciii = chr(int(spi2[-1].strip()))
             flag+=asciii
           #  print(spi2[-1].strip())
    except IndexError:
        print
flagg="QVRN"+flag.split("QVRN")[1]
print(base64.b64decode(flagg.encode()))
flagOut = open("flagWeirdTraffic2.txt","w")
flagOut.write(base64.b64decode(flagg.encode()).decode())
flagOut.close()


