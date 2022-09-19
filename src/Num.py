from math import floor
import Utils
import random

class Num:

    def __init__(self, c, s):
        """Creates a list that represents a column of numbers in the csv
        
        Parameters:
        c (int): The columns position,
        s (str): The columns name"""
        self.n = 0

        if c is not None:
            self.at = c
        else:
            self.at = 0

        if s is not None and s != '':
            self.name = s
            # w = ((s or ""):find"-$" and -1 or 1)
            # if a '-' is found always returns -1, returns 1 otherwise        
            self.w = -1 if (s[len(s)-1] == '-') else 1
        else:
            self.name = ''
            self.w = 1
        self._has = []
        self.lo = float('inf')
        self.hi = float('-inf')
        self.isSorted = True

    # function Num:nums()
    def nums(self):
        """Sorts the numbers in the list
        
        Returns:
        The sorted list"""
        if type(self) != Num:
            return
        if not self.isSorted:
            self._has.sort()
            self.isSorted = True
        return self._has

    # function for Num:add(v,   pos)
    def add (self, v):
        """Adds a number to the list. The list only holds a certain amount of numbers
        depending on the 'nums' argument in 'the' from Utils. Uses resevoir sampling.
        
        Parameters:
        v (number): The value being added to the list"""
        if v!="?":
            self.n += 1
            if self.lo > v:  # checks for lowest value
                self.lo=v
            if self.hi < v:  # checks for highest value
                self.hi=v
            if len(self._has) < Utils.the['nums']: # checks if there is enough space in _has
                pos=len(self._has)
            elif random.uniform(0, 1) < Utils.the['nums']/self.n:
                pos=random.randint(0, len(self._has) - 1) # if not, chooses a random position for the new value                
            if 'pos' in locals(): # Check if pos has been defined
                self.isSorted=False
                if pos < len(self._has):
                    self._has[pos]=float(v) # Adds the new value to _has
                else:
                    self._has.insert(pos, float(v)) # Adds the new value to _has
        else:
            return

    # function for Num:div()
    def div(self):
        """Calculates the standard deviation of the list of numbers
        
        Returns:
        The standard deviation"""
        a = self.nums()
        return (self.per(a,.9)-self.per(a,.1))/2.58

    def per(self,t,p):
        """Helper method for calculating the standard deviation"""
        if p is None:
            p = .5
        p= floor((p*len(t))+.5)
        return t[max(1,min(len(t),p))]

    # function for Num:mid()
    def mid(self):
        """Calculates the median number from the list
        
        Returns:
        The median number from the list"""
        self.nums()
        if len(self._has)%2==1: # checks if the length of _has is odd or even
            return self._has[int((len(self._has)-1)/2)]
        else: #if even, divide the middle two values to get the median
            return float((self._has[int(len(self._has)/2)] + self._has[int((len(self._has)-2)/2)])/2) 
