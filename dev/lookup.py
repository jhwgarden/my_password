"""
encode yaml- formatted accounts
"""

from lib.encoder import decode

import re, yaml

if __name__=="__main__":
    try:
        import sys, os
        if len(sys.argv) < 4:
            raise RuntimeError("Please enter filename, pattern, secretkey")
        filename, pattern, secretkey = sys.argv[1:4]
        if not os.path.isfile(filename):
            raise RuntimeError("Path is not a file")
        if not filename.endswith("yaml"):
            raise RuntimeError("File must be yaml encoded")
        accounts=yaml.load(file(filename).read())
        found=[]
        for account in accounts:
            if re.search(pattern, account["name"], re.I)!=None:
                account["password"]=decode(account["password"], secretkey)
                found.append(account)
        print yaml.safe_dump(found, default_flow_style=False)
    except RuntimeError, error:
        print "Error: %s" % str(error)

