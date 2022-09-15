import re


help="""   
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license

USAGE: lua seen.lua [OPTIONS]

OPTIONS:
 -e  --eg        start-up example                      = nothing
 -d  --dump      on test failure, exit with stack dump = false
 -f  --file      file with csv data                    = data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      number of nums to keep                = 512
 -s  --seed      random number seed                    = 10019
 -S  --seperator feild seperator                       = , """

def coerce(s):
    def fun(s1):
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1
    if s.isnumeric():
        return int(s)
    else:
        try:
            return float(s)
        except ValueError:
            return fun(s.strip())
 

the = {}
for k,v in re.findall(r'\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help):
    the[k] = coerce(v)

def cli(t):
    return

def csv(fname, fun):
    sep = "([^"+the['seperator']+"]+)"
    src = open(fname, "r")
    while True:
        s = src.readline()
        if not s:
            return src.close()
        else: 
            t={}
            for s1 in re.findall(r'' + sep, s):
                t[len(t)] = coerce(s1)
            fun(t)

def o(t):
    return

def oo(t):
    print(o(t))
    return t
