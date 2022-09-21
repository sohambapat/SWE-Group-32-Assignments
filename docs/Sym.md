Module Sym
==========

Classes
-------

`Sym(c, s)`
:   Creates a dict that represents a column of symbols in the csv
    
    Parameters:
    c (int): The columns position,
    s (str): The columns name

    ### Methods

    `add(self, v)`
    :   Adds a value to the column
        
        Parameters:
        v (str): The value being added

    `div(self)`
    :   Calculates the entropy of all the items in the column
        
        Returns:
        The calculated entropy

    `mid(self)`
    :   Calculates the mode of all the items in the column
        
        Returns:
        The symbol that appeared the most