"""
script to see why passwords of len(16) don't get decoded
"""

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

def trim_text(text, c=DefaultPackChar):
    count=0
    for i in range(len(text)):
        j=len(text)-(i+1)
        if text[j]!=c:
            break
        count+=1
    return text[:-count]

def encode(text, secretkey):
    secretkey=pack_secretkey(secretkey)
    cipher=AES.new(secretkey, AES.MODE_ECB)                
    return base64.b64encode(cipher.encrypt(pack_text(text)))

def decode(text, secretkey):
    secretkey=pack_secretkey(secretkey)
    cipher=AES.new(secretkey, AES.MODE_ECB)                
    return trim_text(cipher.decrypt(base64.b64decode(text)))


if __name__=="__main__":
    try:
        text, secretkey = "krazivayamalchik", "welcometothepleasuredome"
        from lib.encoder import encode, decode
        encodedtext=encode(text, secretkey)
        print encodedtext
        print "**%s**" % decode(encodedtext, secretkey)
    except RuntimeError, error:
        print "Error: %s" % str(error)

