import re
import string # Regex library, allowed by Q36 on discord
from Num import Num
from Sym import Sym
from Cols import Cols

class Data:
    def __init__(self, src):
        self.cols = None
        self.rows = []
        if type(src) == string:
            csv(src, self.add())
        else:
            for _, row in src:
                self.add(row)
        return


    # function Data:add()
    def add(self, xs):
        row = []
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row.append(self.rows)
            for _, todo in [(i, j) for i in self.cols.x for j in self.cols.y if i != j]:
                for _, col in todo.items():
                    Cols.add(row.cells[index(col)])
        
