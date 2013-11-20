"""
http://stackoverflow.com/questions/15956952/how-do-i-decrypt-using-hashlib-in-python
"""

from Crypto.Cipher import AES

import base64

"""
AES key must be either 16, 24, or 32 bytes long
"""

def pack_text(text, c=" ", n=16):
    rem=len(text) % n
    return text+c.join(['' for i in range(1+n-rem)])        

def trim_text(text, c=" "):
    count=0
    for i in range(len(text)):
        j=len(text)-(i+1)
        if text[j]!=c:
            break
        count+=1
    return text[:-count]

if __name__=="__main__":
    try:
        import sys 
        if len(sys.argv) < 3:
            raise RuntimeError("Please enter text, secret key")
        text, secretkey = sys.argv[1:3]
        cipher=AES.new(secretkey, AES.MODE_ECB)        
        encoded=base64.b64encode(cipher.encrypt(pack_text(text)))
        print encoded
        decoded=trim_text(cipher.decrypt(base64.b64decode(encoded)))
        print "**%s**" % decoded
    except RuntimeError, error:
        print "Error: %s" % str(error)

