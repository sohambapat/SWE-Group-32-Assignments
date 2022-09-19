from cmath import log

import random

class Sym:
    
    # Constructor Sym:new(c,s) 
    def __init__(self,c,s):
        """Creates a dict that represents a column of symbols in the csv
        
        Parameters:
        c (int): The columns position,
        s (str): The columns name"""
        self.n = 0
        # self.at = c if self.at else 0
        if c is not None:
            self.at = c
        else:
            self.at = 0
        # self.name = s if self.name else ""
        if s is not None:
            self.name = s
        else:
            self.name = ""
        # _has = {}
        self._has = {}
        
    # function sym:add(v)
    def add(self, v):
        """Adds a value to the column
        
        Parameters:
        v (str): The value being added"""
        if v!= "?":
            self.n= self.n+1
            if v in self._has.keys():
                self._has[v]=self._has[v]+1
            else: 
                self._has[v]=1
        else: 
            return
 
    # function sym:div()
    def div(self):
        """Calculates the entropy of all the items in the column
        
        Returns:
        The calculated entropy"""
        e = 0
        for _, n in self._has.items():
            if n > 0 :
                e = e - (n/self.n)*log(n/self.n,2)
        return e

    # function Sym:mid(col,    most,mode) 
    def mid(self):
        """Calculates the mode of all the items in the column
        
        Returns:
        The symbol that appeared the most"""
        most = -1
        for k, v in self._has.items():
            if v > most :
                mode, most = k, v
        return mode
