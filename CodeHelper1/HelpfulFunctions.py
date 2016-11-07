'''
London Lowmanstone IV
Hepful Functions Module
Version 1.5
11/22/2015

Dp (short for deleted print statements)
'''

#Helpful Functions

def getAllIndexes(aList, anObj):
    indexes = []
    for index, item in enumerate(aList):
        if item==anObj:
            indexes.append(index)
    return indexes
            
def allEqual(*args):
    args = list(args)
    for index, value in enumerate(args):
        for i in range(1, len(args)-(index)):
            if value!=args[i]:
                return False
    return True 

def addNameAtts(obj, theList, setTo):
    setToType = type(setTo)
    setToIsIndexable = False
    if (setToType is list) or (setToType is tuple):
        setToIsIndexable = True
        
    if setToIsIndexable:
        for index, name in enumerate(theList):
            #print("setting {} to {}".format(name, setTo[index]))
            setattr(obj, name, setTo[index])
    else:
        for index, name in enumerate(theList):
            setattr(obj, name, setTo)
    #the lesson to be learned here is that how often the variables inside the loop need to be updated is determined by the loop.
    #i.e. if different variables need to be updated depending on certain conditions, either those conditions are checked each time inside the loop, or the loop code has to be written out twice.
        
def completeStrip(line): #strips all the whitespace from a line
    return "".join(line.split())
    
def completeStripAndLower(s):
    ans = completeStrip(s)
    ans = ans.lower()
    return ans
    
#returns the first substring found in between the substring "left" and the substring "right".
#Right now it assumes that left and right only occur once in fullString, but do not take advantage of that.
#returns None if left and right aren't both substrings of fullString
def getSubstringInBetween(fullString, left, right, start = 0):
    getLeft = None
    if left==False:
        getLeft = 0 #go from the start of the string
    else:
        getLeft = fullString.find(left, start) + len(left) #where the left symbol ends
        
    getRight = None
    if right==False:
        getRight = len(fullString) #go to the end of the string
    else:
        getRight = fullString.find(right, max(getLeft, start)) #start searching after the left symbol is found
        
    if getLeft!=-1 and getRight!=-1: #if left and right were found inside the string when searched for
        return fullString[getLeft:getRight] #returns the substring in between the first two symbols.
    else:
        return None #couldn't find the left and right symbols within the line
    