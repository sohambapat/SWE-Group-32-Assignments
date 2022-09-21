Module Num
==========

Classes
-------

`Num(c, s)`
:   Creates a list that represents a column of numbers in the csv
    
    Parameters:
    c (int): The columns position,
    s (str): The columns name

    ### Methods

    `add(self, v)`
    :   Adds a number to the list. The list only holds a certain amount of numbers
        depending on the 'nums' argument in 'the' from Utils. Uses resevoir sampling.
        
        Parameters:
        v (number): The value being added to the list

    `div(self)`
    :   Calculates the standard deviation of the list of numbers
        
        Returns:
        The standard deviation

    `mid(self)`
    :   Calculates the median number from the list
        
        Returns:
        The median number from the list

    `nums(self)`
    :   Sorts the numbers in the list
        
        Returns:
        The sorted list

    `per(self, t, p)`
    :   Helper method for calculating the standard deviation