#function Row:new
class Row:
    # Row holds one record
    def __init__(self, t):
        """Initializes the row from the csv file and creates a copy of the data

        Parameters:
        t (dict): The contents of the row"""
        self.cells=t
        self.cooked = t.copy()
        self.isEvaled = False