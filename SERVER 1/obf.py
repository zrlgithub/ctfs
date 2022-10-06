import os  
from itertools import cycle
import base64



def _xor(plain_text, key):
    
    
    pt = plain_text
    len_key = len(key)
    encoded = []
      
    for i in range(0, len(pt)):
        encoded.append(pt[i] ^ key[i % len_key])
    return bytes(encoded)

key = open("key_log.log",'r').read()

content = key.replace("CLIENT_RANDOM","")
content = content.replace(" ","")

binary_content = bytes.fromhex(content)

new_key =  os.urandom(1)

obf_1 = _xor(binary_content,new_key)

g = open("ofuscated_keys","w").write(base64.b64encode(obf_1).decode())

