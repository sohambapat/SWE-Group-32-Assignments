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

# function for Num:add(v,   pos)
def add (v, pos, self, n, nums): #nums replaces the.nums
    if v!="?":
        self.n=n+1
        if self.lo > v:  # checks for lowest value
            self.lo=v
        if self.hi < v:  # checks for highest value
            self.hi=v
        if len(self._has) < nums: # checks if there is enough space in _has
            pos=len(self._has)+1 
        else:
            pos=random.randint(0,len(self._has)) # if not, chooses a random position for the new value
        if pos:
            self.isSorted=False 
            self._has[pos]=float(v) # Adds the new value to _has
    else:
        return

# function for Num:div()
def stdDev(self):
    a = nums(self)
    return (per(a,.9)-per(a,.1))/2.58

# function for Num:mid()
def median(self):
    if self.isSorted==False: # needs to be sorted to find the median 
        return
    else:
        if len(self._has)%2==1: # checks if the length of _has is odd or even
            return self._has[(len(self._has)-1)/2]
        else: #if even, divide the middle two values to get the median
            return float(self._has[len(self._has)/2] - self._has[(len(self._has)-2)/2]) 
