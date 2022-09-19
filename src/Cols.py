import re # Regex library, allowed by Q36 on discord
from Num import Num
from Sym import Sym

class Cols:

    # names is a table
    def __init__(self, names):
        """Creates a list containing all of the columns. Creates column
        objects as Nums or Syms depending on the name of the column.
        
        Parameters:
        names (list): List of the names of all the columns"""
        # Changed these from dicts to lists because the lua
        # push method sets the key to index value, just like a list
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []

        # Left names as a dict, but can easily be changed to list
        # if wanted. c would be index and s would be value at index
        for c, s in names.items():
            if re.match("^[A-Z]+", s):
                col = Num(c, s)
            else:
                col = Sym(c, s)
            self.all.append(col)
            if re.search(":$", s) is None:
                if re.search("[!+-]", s):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if re.search("!$", s):
                    self.klass=col