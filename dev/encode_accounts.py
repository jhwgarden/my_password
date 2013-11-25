"""
encode yaml- formatted accounts
"""

from lib.encoder import encode

import yaml

if __name__=="__main__":
    try:
        import sys, os
        if len(sys.argv) < 3:
            raise RuntimeError("Please enter filename, secretkey")
        filename, secretkey = sys.argv[1:3]
        if not os.path.isfile(filename):
            raise RuntimeError("Path is not a file")
        if not filename.endswith("yaml"):
            raise RuntimeError("File must be yaml encoded")
        accounts=yaml.load(file(filename).read())
        for account in accounts:
            if account["password"]:
                account["password"]=encode(account["password"], secretkey)
        dest=file("tmp/encoded_accounts.yaml", 'w')
        dest.write(yaml.safe_dump(accounts, default_flow_style=False))
        dest.close()
    except RuntimeError, error:
        print "Error: %s" % str(error)

