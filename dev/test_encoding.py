"""
script to test encoding
"""

if __name__=="__main__":
    try:
        import sys 
        if len(sys.argv) < 3:
            raise RuntimeError("Please enter text, secret key")
        text, secretkey = sys.argv[1:3]
        from lib.encoder import encode, decode
        encodedtext=encode(text, secretkey)
        print encodedtext
        print "**%s**" % decode(encodedtext, secretkey)
    except RuntimeError, error:
        print "Error: %s" % str(error)

