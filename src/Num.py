class Num:

    def __init__(self, c, s):
        self.n = 0

        if c is not None:
            self.at = c
        else:
            self.at = 0

        if s is not None:
            self.name = s
        else:
            self.name = ''
        
        self._has = []
        self.lo = float('inf')
        self.hi = float('-inf')
        self.isSorted = True

        # w = ((s or ""):find"-$" and -1 or 1)
        # if a '-' is found always returns -1, returns 1 otherwise        
        self.w = -1 if (s[len(s)-1] == '-') else 1
        
def nums( n ):
    if type(n) != Num:
        return
    if not n.isSorted:
        n._has.sort()
        n.isSorted = True
    return n._has
