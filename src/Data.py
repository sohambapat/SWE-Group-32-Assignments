from Cols import Cols
from Row import Row
import Utils
from math import floor

class Data:
    def __init__(self, src):
        self.cols = None
        self.rows = []
        if isinstance(src, str):
            def function(row):
                self.add(row)
            Utils.csv(src, function)
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
            if isinstance(xs, Row):
                row = xs
                self.rows.append(xs)
            else:
                row = Row(xs)
                self.rows.append(row)
            for _, col in enumerate(self.cols.x):
                col.add(row.cells[col.at])
            for _, col in enumerate(self.cols.y):
                col.add(row.cells[col.at])

    def stats(self, places, showCols, fun):
        if showCols is None:
            showCols = self.cols.y
        if fun is None:
            fun = "mid"
        t = {}
        for _,col in showCols.items():
            v = fun(col)
            if type(v) == (int or float):
                if places is not None:
                    mult = 10**places
                else:
                    mult = 10**2
                v = floor(v * mult + 0.5) / mult
            else:
                v = v
            t[col.name] = v
        return t