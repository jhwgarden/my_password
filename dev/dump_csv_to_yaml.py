import csv, yaml

if __name__=="__main__":
    reader=csv.reader(file("/home/justin/Dropbox/accounts/hufton.csv"))
    titles=reader.next()
    titles=["account", "username", "password"] # override
    struct=[dict([(title, row) 
                  for title, row in zip(titles, row)])
            for row in reader]
    dest=file("tmp/accounts.yaml", 'w')
    dest.write(yaml.safe_dump(struct, default_flow_style=False))
    dest.close()
