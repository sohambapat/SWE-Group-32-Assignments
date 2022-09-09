import re # Regex library, allowed by Q36 on discord
from Num import Num
from Sym import Sym

class Cols:

    # names is a table
    def __init__(self, names):
        # Left these as dicts where key is col numbers starting from 0
        self.names = names
        self.all = {}     # Will have to go back to Num to change
        self.klass = None # list type from [] to {} so all columns
        self.x = {}       # can be saved easily
        self.y = {}

        # For c, s in pairs(names) do
        # For key, value in pairs(t) do
        for c, s in names.items():
            if re.match("^[A-Z]+", s):
                col = Num(c, s)
            else:
                col = Sym(c, s)
            self.all[c] = col
            if re.search(":$", s) is None:
                if re.search("[!+-]", s):
                    self.y[c] = col
                else:
                    self.x[c] = col
                if re.search("!$", s):
                    self.klass=col
