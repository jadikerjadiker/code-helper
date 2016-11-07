'''
File Finder Helper Methods
SymbolPageReader Class
Version 1.14
12/14/2015

fixed getInBetweenSymbolsFromCurrent so that it wouldn't get things it shouldn't be able to.
'''

#sets the position in the file to the character after where it found the given string.
#the string can occur over multiple lines if the string includes a newline character.
#also returns this position in bytes from the start of the file.
def findStringFromCurrent(openFile, string):
    #upgrade: could be optimized to delete lines that it knows does not contain the start of the string at all. Otherwise it's holding the entire page in memory by the end.
    #nts: readline() and read() work with seek() and tell(). next() and enumerate() do not.
    startPoint = openFile.tell()
    allLines = ""
    line = openFile.readline()
    allLines+=line
    check = allLines.find(string)
    while check==-1 and line!="":
        line = openFile.readline()
        allLines+=line
        check = allLines.find(string)
        
    if check!=-1: #if I did find it
        openFile.seek(startPoint+check+len(string), 0) #go to the character after the string.
        return openFile.tell() #return where you are at (in case they want the value for some reason.)
        
    else: #got to the end of the file without finding the string
        return None

#starts at the current position in the open file openFile and returns the text in between the openSym and closeSym
#returns None if it can't find the openSym or closeSym
def getInBetweenSymbolsFromCurrent(openFile, openSym, closeSym):
    allSearch = "" #the string that will hold all the text this function is looking at
    openSymPos = -1 #position within allSearch that the starting symbol was found (it's truncated from this point onwards once found)
    closeSymPos = -1 #position within the truncated allSearch that the closing symbol was found.
    nextLine = openFile.readline()
    #will return if it gets what it wants.
    EMPTY_CLOSE_ASSUME = "\n" #if the closing symbol is an empty string, then assume it's actually a newline
    if openSym == "": #if it's an empty string, assume we found it right away
        openSymPos = 0
    if closeSym == "": #if the closing symbol is empty, set it to the programmer's constant EMPTY_CLOSE_ASSUME
        closeSym = EMPTY_CLOSE_ASSUME
    while nextLine!="":
        allSearch+=nextLine
        if openSymPos==-1: #if I haven't found the starting symbol yet
            openSymPos = allSearch.find(openSym)
            if openSymPos!=-1: #just found it so cut off all the stuff we don't need
                allSearch = allSearch[openSymPos+len(openSym):]
                closeSymPos = allSearch.find(closeSym) #then, look for the closeSym since we won't trigger the else yet.
        else:
            closeSymPos = allSearch.find(closeSym)
            
        if openSymPos!=-1 and closeSymPos!=-1:
            return allSearch[:closeSymPos] #go from the end of the openSym (we alread spliced it so that it starts at the start of openSym) up to the start of the closeSym
        nextLine = openFile.readline()
    #treat an EOL as a new line
    if openSymPos!=-1 and closeSym[-1:]=="\n": #also make sure we found the opening symbol before even checking for odd ending stuff.
        closeSym = closeSym[:-1] #strip off the last newline in the closeSym
        #if all it was looking for was a newline, or if there was something before the newline to search for, make sure it matches and then return all I've gotten minus the closeSym.
        if closeSym=="" or allSearch[-len(closeSym):]==closeSym:
            return allSearch[:len(allSearch)-len(closeSym)]
    
    #default fail return; couldn't find both of the symbols
    return None