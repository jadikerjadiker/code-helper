def blank25Table():
    return [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

def maxn(table):
    last = -1
    for i, item in enumerate(table):
        if item!=None:
            last = i
    return last

def print25Table(t):
    for i in range(1, 26):
        if t[i]!=None:
            print("{}: {}".format(i, t[i]))

def printablePiece(p):
    return "{} at {} with dir {}".format(p.type, p.pos, p.direction)

def printPieceList(l):
    print("printPieceList unabailable at the moment.")

def getElementFirstKey(ele, table):
    for index, thing in enumerate(table):
        if ele == thing:
            return index
    return None
        
