"""
script to convert existing csv account format to yaml
"""

import yaml

if __name__=="__main__":
    try:
        import sys
        if len(sys.argv) < 2:
            raise RuntimeError("Please enter filename")
        filename=sys.argv[1]
        import os
        if not os.path.isfile(filename):
            raise RuntimeError("File not found")
        import csv
        reader=csv.reader(file(filename))
        titles=reader.next()
        titles=["account", "username", "password"] # override
        struct=[dict([(title, row) 
                      for title, row in zip(titles, row)])
                for row in reader]
        dest=file("tmp/accounts.yaml", 'w')
        dest.write(yaml.safe_dump(struct, default_flow_style=False))
        dest.close()
    except RuntimeError, error:
        print "Error: %s" % str(error)
