#!/usr/bin/env python

# The top line informs UNIX/LINUX that the current file should be executed 
# as a python script. Lines should never exceed 79 characters (see style
# guide).

"""Module Description
The docstring at the top of the file appears in the "Description" field of 
the help command. That is, if you load a python interpreter the following 
makes the docstring visible:

  $ python
  >>> import your_module
  >>> help(your_module)

Note the name "your_module" is just the filename without the .py extension.
You can check this field for any other python module (numpy, sympy, etc.) 
to get an idea about how module documentation is usually handled.
"""

# This is the body of the module.  Place all global constants, function 
# definitions, and class definitions here.  No free-floating executable
# code should appear in a module.

# Minimize the use of global constants.
CONSTANT1 = 0

def function1(arg1, kwarg1=defaultvalue, *args, **kwargs):
    """Function docstring
    All functions should have their own documentation via docstrings.
    Standard indent size in python is 4 spaces, no tabs. Arguments are
    positional, unless given a default value as a keyword-argument.
    Here args is a list of all positional arguments beyond those listed.
    Here kwargs is a list of all keyword arguments beyond those listed.
    """
    pass

def main(argv):
    """Main function
    See below for why this would exist. The argv argument lists command
    line arguments taken from sys.argv in the main block below.
    """
    pass

def test_function1():
    """Test function for nosetests
    Any function starting with name test_ will be automatically run
    by nosetests. Use an assert command to test a Boolean statement
    about how your code executed.  If the assert fails, it throws
    an exception, which is caught by nosetests and reported.
    Anything that is printed to the screen during this function is
    suppressed unless there is a failure, where it can be used for
    debugging.
    """
    assert True

class class1(object):
    """Class docstring
    """
    def __init__(self, *args, **kwargs):
        """Class constructor
        The self parameter refers to the object instance (identical to
        'this' in C++/Java).
        """
        pass
    
    def method1(self, *args, **kwargs):
        """Method docstring
        """
        pass
    
# After the body of the module, you can optionally create a section to
# house executable code.

if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    from sys import argv
    main(argv)
