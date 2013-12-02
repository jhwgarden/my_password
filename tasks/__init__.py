import os, re, yaml

class BaseTask:

    @classmethod
    def validate(self, *args, **kwargs):
        pass

    def initialise(self, *args, **kwargs):
        pass

EncodedFields=["password", "secretkey"]

SecretKeyFile="tmp/secretkey.txt"

def load_secretkey():
    try:
        return re.sub("\\s", "", file(SecretKeyFile).read())
    except:
        raise RuntimeError("Secret key does not exist")

def encode_accounts(accounts, secretkey):
    from lib.encoder import encode
    for account in accounts:
        for attr in EncodedFields:
            if attr in account:
                account[attr]=encode(account[attr], secretkey)

def decode_accounts(accounts, secretkey):
    from lib.encoder import decode
    for account in accounts:
        for attr in EncodedFields:
            if attr in account:
                account[attr]=decode(account[attr], secretkey)

class EncodeTask(BaseTask):

    @classmethod
    def validate(self, *args, **kwargs):
        if len(args)==0:
            raise RuntimeError("Please enter src")
        if not os.path.isfile(args[0]):
            raise RuntimeError("Src file not found")        
        if not args[0].endswith("yaml"):
            raise RuntimeError("Src must be a yaml file")

    def initialise(self, *args, **kwargs):        
        self.src=args[0]

    def run(self, *args, **kwargs):        
        secretkey=load_secretkey()
        accounts=yaml.load(file(self.src).read())
        encode_accounts(accounts, secretkey)
        dest=file("tmp/encoded.yaml", 'w')
        dest.write(yaml.safe_dump(accounts, default_flow_style=False))
        dest.close()

class DecodeTask(BaseTask):

    @classmethod
    def validate(self, *args, **kwargs):
        if len(args)==0:
            raise RuntimeError("Please enter src")
        if not os.path.isfile(args[0]):
            raise RuntimeError("Src file not found")        
        if not args[0].endswith("yaml"):
            raise RuntimeError("Src must be a yaml file")

    def initialise(self, *args, **kwargs):        
        self.src=args[0]

    def run(self, *args, **kwargs):        
        secretkey=load_secretkey()
        accounts=yaml.load(file(self.src).read())
        decode_accounts(accounts, secretkey)
        dest=file("tmp/decoded.yaml", 'w')
        dest.write(yaml.safe_dump(accounts, default_flow_style=False))
        dest.close()


class SearchTask(BaseTask):

    @classmethod
    def validate(self, *args, **kwargs):
        if len(args) < 2:
            raise RuntimeError("Please enter src, pattern")
        if not os.path.isfile(args[0]):
            raise RuntimeError("Src file not found")        
        if not args[0].endswith("yaml"):
            raise RuntimeError("Src must be a yaml file")

    def initialise(self, *args, **kwargs):
        self.src, self.pattern = args[:2]

    def run(self, *args, **kwargs):
        secretkey=load_secretkey()
        accounts=yaml.load(file(self.src).read())
        decode_accounts(accounts, secretkey)
        print yaml.safe_dump([account for account in accounts
                              if re.search(self.pattern, account["name"], re.I)!=None],
                             default_flow_style=False)


