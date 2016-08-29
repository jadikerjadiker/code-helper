#Made in 2015 by London Lowmanstone IV
#functions used to aid in programming and debugging

#returns a table with 26 "None"s.
#This code was ported from Lua, whose table indexes start at 1, so usually any code using this function will never edit the first element
def blank25Table():
    return [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

#returns the the "length" of the table
def maxn(table):
    last = -1
    for i, item in enumerate(table):
        if item!=None:
            last = i
    return last

#prints out a 25Table (any table created from blank25Table)
def print25Table(t):
    for i in range(1, 26):
        if t[i]!=None:
            print("{}: {}".format(i, t[i]))

#returns a string that represents a piece
def printablePiece(p):
    return "{} at {} with dir {}".format(p.type, p.pos, p.direction)

#gets the key of the first time an element appears in a table
#returns none if the element does not occur in the table
def getElementFirstKey(ele, table):
    for index, thing in enumerate(table):
        if ele == thing:
            return index
    return None
        
