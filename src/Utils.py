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
"""Command line arguments for 'the' to use when initializing."""


def init():
    """Initializes the value of 'the' using the arguments from 'help'."""
    global the
    the = {}
    for k,v in re.findall(r'\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help):
        the[k] = coerce(v)

def coerce(s):
    """Converts a string into the appropriate type and trims if necessary.
    
    Parameters:
    s (str): String being converted to another type
    
    Returns:
    Returns the string in its appropriate type"""
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

def csv(fname, fun):
    """Reads the information from a csv file
    
    Parameters:
    fname (str): The name of the file to be opened,
    fun (function): A function with one parameter expecting a dict"""
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
    """Formats a dict into a readable format and prints it

    Parameters:
    t (dict): Dict being printed
    
    Returns: The string that is printed"""
    if not (isinstance(t, dict) or isinstance(t, list)):
        return str(t)
    def show(k, v):
        if not re.compile(r'^_').search(str(k)):
            v = o(v)
            if len(t) != 0:
                return ":{k} {v}".format(k = k, v = v)
            else:
                return str(v)
    u = []
    if isinstance(t, dict):
        for k, v in t.items():
            u.append(show(k,v))
        if len(t) != 0:
            u.sort()
        return "{"+' '.join(map(str, u))+"}"
    if isinstance(t, list):
        for i,v in enumerate(t):
            u.append(str(v))
        if len(t) != 0:
            u.sort()
        return "{"+' '.join(u)+"}"

def oo(t):
    """Prints a table and returns it
    
    Parameters:
    t (dict): Dict to be printed and returned unchanged
    
    Returns:
    The parameter given with no changes made"""
    print(o(t))
    return t