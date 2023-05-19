import clingo
from config import *

def findPits():
    return

def getModel():
    # This is temporary and will be replaced.

    model = '''
    {a}.
    b :- a.
    :- not b

    '''
    

    # Use nqueens to create pit creation algorithm.
    # Use nqueens to add points squares