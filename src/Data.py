from Cols import Cols
from Row import Row
import Utils
from math import floor

class Data:
    def __init__(self, src):
        """Initializes the data from the csv. Responsible for 
        opening the csv and storing all of the data. Keeps track 
        of the column headers and the row's information.
        
        Parameters:
        src (str): The name of the csv file"""
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
        """Adds a row from the csv to the data. If it is the first
        row of the csv set the row to be the headers (cols).
        
        Parameters:
        xs (Row): The Row object being added to the data,
        xs (str): The string to be converted to a row object and added to the data"""
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
        """Takes stats from the columns of data and returns them
        
        Parameters:
        places (int): The amount of decimal places (default 2),
        showCols (list): A list of all the columns,
        fun (function): A function that gathers the statistic from the data in the column
        
        Returns:
        A list consisting of the statistic for each column in their respective index"""
        if showCols is None:
            showCols = self.cols.y
        if fun is None:
            fun = "mid"
        t = {}
        for _,col in enumerate(showCols):
            v = fun(col)
            if isinstance(v, int) or isinstance(v, float):
                if places is not None:
                    mult = 10**places
                else:
                    mult = 10**2
                v = floor(v * mult + 0.5) / mult
            else:
                v = v
            t[col.name] = v
        return t