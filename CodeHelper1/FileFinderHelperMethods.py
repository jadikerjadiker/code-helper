'''
File Finder Helper Methods
SymbolPageReader Class
Version 1.7
12/4/2015

made findStringFromCurrent() work for multiline strings
'''

#todo temp logs
from DebugHelper import *
#sets the position in the file to the character after where it found the given string.
#the string can occur over multiple lines if the string includes a newline character.
#also returns this position in bytes from the start of the file.
def findStringFromCurrent(openFile, string):
    #upgrade: could be optimized to delete lines that it knows does not contain the start of the string at all. Otherwise it's holding the entire page in memory by the end.
    #nts: readline() and read() work with seek() and tell(). next() and enumerate() do not.
    log("called with string '{}'".format(string))
    startPoint = openFile.tell()
    log("startPoint is {}".format(startPoint))
    log("Lines read:")
    allLines = ""
    line = openFile.readline()
    allLines+=line
    check = allLines.find(string)
    while check==-1 and line!="":
        log(line)
        line = openFile.readline()
        allLines+=line
        check = allLines.find(string)
        
    if check!=-1: #if I did find it
        openFile.seek(startPoint+check+len(string), 0) #go to the character after the string.
        log("found it at {}".format(openFile.tell()))
        return openFile.tell() #return where you are at (in case they want the value for some reason.
    else: #got to the end of the file without finding the string
        log("Didn't find it")
        return None

#starts at the current position in the open file openFile and returns the text in between the openSym and closeSym
#returns None if it can't find the openSym or closeSym
def getInBetweenSymbolsFromCurrent(openFile, openSym, closeSym):
    allSearch = ""
    openSymPos = -1
    closeSymPos = -1
    nextLine = openFile.readline()
    #will return if it gets what it wants.
    while nextLine!="":
        allSearch+=nextLine
        if openSymPos==-1: #if I haven't found the starting symbol yet
            openSymPos = allSearch.find(openSym)
            if openSymPos!=-1: #just found it so cut off all the stuff we don't need
                allSearch = allSearch[openSymPos:]
                closeSymPos = allSearch.find(closeSym) #then, look for the closeSym since we won't trigger the else yet.
        else:
            closeSymPos = allSearch.find(closeSym)
            
        if openSymPos!=-1 and closeSymPos!=-1:
            return allSearch[len(openSym):closeSymPos] #go from the end of the openSym (we alread spliced it so that it starts at the start of openSym) up to the start of the closeSym
        nextLine = openFile.readline()
    #Couldn't find one of the symbols, returning None
    return None