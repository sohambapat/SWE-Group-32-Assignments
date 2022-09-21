Module Utils
============

Variables
---------

    
`help`
:   Command line arguments for 'the' to use when initializing.

Functions
---------

    
`coerce(s)`
:   Converts a string into the appropriate type and trims if necessary.
    
    Parameters:
    s (str): String being converted to another type
    
    Returns:
    Returns the string in its appropriate type

    
`csv(fname, fun)`
:   Reads the information from a csv file
    
    Parameters:
    fname (str): The name of the file to be opened,
    fun (function): A function with one parameter expecting a dict

    
`init()`
:   Initializes the value of 'the' using the arguments from 'help'.

    
`o(t)`
:   Formats a dict into a readable format and prints it
    
    Parameters:
    t (dict): Dict being printed
    
    Returns: The string that is printed

    
`oo(t)`
:   Prints a table and returns it
    
    Parameters:
    t (dict): Dict to be printed and returned unchanged
    
    Returns:
    The parameter given with no changes made