import re # Regex library, allowed by Q36 on discord
from Num import Num
from Sym import Sym
from Cols import Cols

class Data:
    def __init__(self):
        return


    # function Data:add()
    def add(self, xs):
        row = []
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row.append(self.rows, xs.cells, xs)
            for _, todo in [(i, j) for i in self.cols.x for j in self.cols.y if i != j]:
                for _, cols in todo.items():
                    Cols.add(row.cells[col.at])
        
