import os, re

class BaseTask:

    @classmethod
    def validate(self, *args, **kwargs):
        pass

    def initialise(self, *args, **kwargs):
        pass

SecretKeyFile="tmp/secretkey.txt"

def load_secretkey():
    try:
        return re.sub("\\s", "", file(SecretKeyFile).read())
    except:
        raise RuntimeError("Secret key does not exist")

class EncodeTask(BaseTask):

    @classmethod
    def validate(self, *args, **kwargs):
        pass

    def initialise(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        print load_secretkey()
        print "encode"

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

