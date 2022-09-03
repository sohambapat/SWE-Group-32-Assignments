from cmath import log


class Sym:
    # Constructor Sym:new(c,s) 
    def __init__(self,c,s):
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
    def add(self,v):
        if v!= "?":
            self.n= self.n+1
            if self._has[v] is not None:
                self._has[v]=self._has[v]+1
            else: self._has[v]=1

        else: return
 

    def div(self):
        e = 0
        for _, n in self._has.items():
            if n > 0 :
                e = e - (n/self.n)*log(n/self.n,2)
        return e

    # function Sym:mid(col,    most,mode) 
    def mid(self, col, mode, most=-1):
        for k, v in self._has.items():
            if v > most :
                mode, most = k, v
        return mode
    
