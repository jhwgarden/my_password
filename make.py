#!/usr/bin/python

import os, re

"""
http://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class
"""

def get_module_from_name(name):
    mod=__import__(name)
    components=name.split('.')
    for comp in components[1:]:
        mod=getattr(mod, comp)
    return mod

def get_class_from_module(mod, classname):
    mod=__import__(mod.__name__, fromlist=[classname])
    return getattr(mod, classname)

def list_modules(root):
    def search(tokens, modules):
        path="/".join(tokens)
        for entry in os.listdir(path):
            if not entry.endswith("py"):
                continue
            newtokens=tokens+[entry]
            newpath="/".join(newtokens)
            if os.path.isdir(newpath):
                search(newtokens, modules)
            else:
                newtokens[-1]=newtokens[-1][:-3] # remove py
                if newtokens[-1]=="__init__":
                    newtokens.pop()
                modules.append(".".join(newtokens))
    modules=[]
    search([root], modules)
    return modules

"""
http://stackoverflow.com/questions/12011091/trying-to-implement-python-testsuite
"""

"""
NB if MyTasks is defined in models/__init__.py and models/match.py imports * from models, MyTasks will appear as models.MyTasks and models.match.MyTasks; so need to check for uniqueness on classname rather than module path
"""

def get_task_classes(roots):
    classes={}
    for root in roots:
        for modname in list_modules(root):
            mod=get_module_from_name(modname)
            for name in dir(mod):
                if (name not in classes and
                    name.endswith("Task")):
                    klass=get_class_from_module(mod, name)
                    classes[name]=klass
    return classes

if __name__=="__main__":
    try:
        import sys
        if len(sys.argv) < 2:
            raise RuntimeError("Please enter taskname, *args")
        taskname=sys.argv[1]
        args, kwargs = [], {}
        for argval in sys.argv[2:]:
            if re.search("^\\w+\\=\\w+$", argval):
                key, value = argval.split("=")
                kwargs[key]=value
            else:
                args.append(argval)
        taskclasses=get_task_classes(["tasks"])
        def get_task_classname(taskname):
            return "%sTask" % "".join([tok.lower().capitalize()
                                       for tok in taskname.split("_")])        
        taskclassname=get_task_classname(taskname)
        if taskclassname not in taskclasses:
            raise RuntimeError("Task not found")
        taskclass=taskclasses[taskclassname]
        taskclass.validate(*args, **kwargs)        
        task=taskclass()
        task.initialise(*args, **kwargs)
        task.run(*args, **kwargs)
    except RuntimeError, error:
        print "Error: %s" % str(error)
