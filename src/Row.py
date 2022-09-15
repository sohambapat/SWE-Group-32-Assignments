#function Row:new
class Row:

    # Row holds one record
    def __init__(self, t):
        self.cells=t
        self.cooked = t.copy()
        self.isEvaled = False