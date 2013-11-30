def trim_text(text, c=' '):
    i=0
    for i in range(len(text)):
        if text[-i]!=c:
            break
    return text[-i:]

for sample in ["foobar", 
               "foobar ", 
               "krazivayamalchik",
               "krazivayamalchik "]:
    print "**%s**" % trim_text(sample)

