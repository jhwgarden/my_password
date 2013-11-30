"""
http://stackoverflow.com/questions/15956952/how-do-i-decrypt-using-hashlib-in-python
"""

from Crypto.Cipher import AES

import base64

"""
AES key must be either 16, 24, or 32 bytes long
"""

AESCipherSizes=[16, 24, 32]
DefaultPackChar=" "
DefaultSize=16

def pack_text(text, c=DefaultPackChar, n=DefaultSize):
    rem=len(text) % n
    return text if rem==0 else text+c.join(['' for i in range(1+n-rem)])  

def pack_secretkey(text):
    for sz in AESCipherSizes:
        if len(text) <= sz:
            return pack_text(text, n=sz)
    return text[:sz]

def trim_text(text, c=' '):
    return c.join([tok for tok in text.split(c)
                   if tok!=''])

def encode(text, secretkey):
    secretkey=pack_secretkey(secretkey)
    cipher=AES.new(secretkey, AES.MODE_ECB)                
    return base64.b64encode(cipher.encrypt(pack_text(text)))

def decode(text, secretkey):
    secretkey=pack_secretkey(secretkey)
    cipher=AES.new(secretkey, AES.MODE_ECB)                
    return trim_text(cipher.decrypt(base64.b64decode(text)))

