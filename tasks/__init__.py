import os, re, yaml

class BaseTask:

    @classmethod
    def validate(self, *args, **kwargs):
        pass

    def initialise(self, *args, **kwargs):
        pass

from lib.encoder import encode, decode

EncodedFields=["password"]

SecretKeyFile="tmp/secretkey.txt"

def load_secretkey():
    try:
        return re.sub("\\s", "", file(SecretKeyFile).read())
    except:
        raise RuntimeError("Secret key does not exist")

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
        for account in accounts:
            for attr in EncodedFields:
                if account[attr]:
                    account[attr]=encode(account[attr], secretkey)
        dest=file("tmp/encoded.yaml", 'w')
        dest.write(yaml.safe_dump(accounts, default_flow_style=False))
        dest.close()

class SearchTask(BaseTask):

    @classmethod
    def validate(self, *args, **kwargs):
        pass

    def initialise(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        print "search"

class AddTask(BaseTask):

    @classmethod
    def validate(self, *args, **kwargs):
        pass

    def initialise(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        print "add"

