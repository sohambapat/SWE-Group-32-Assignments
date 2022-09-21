Module Data
===========

Classes
-------

`Data(src)`
:   Initializes the data from the csv. Responsible for 
    opening the csv and storing all of the data. Keeps track 
    of the column headers and the row's information.
    
    Parameters:
    src (str): The name of the csv file

    ### Methods

    `add(self, xs)`
    :   Adds a row from the csv to the data. If it is the first
        row of the csv set the row to be the headers (cols).
        
        Parameters:
        xs (Row): The Row object being added to the data,
        xs (str): The string to be converted to a row object and added to the data

    `stats(self, places, showCols, fun)`
    :   Takes stats from the columns of data and returns them
        
        Parameters:
        places (int): The amount of decimal places (default 2),
        showCols (list): A list of all the columns,
        fun (function): A function that gathers the statistic from the data in the column
        
        Returns:
        A list consisting of the statistic for each column in their respective index