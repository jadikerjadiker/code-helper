'''
FileFinderHelper0p0 Class
London Lowmanstone IV
Version 2.2
12/4/2015

debugging
'''

'''
The goal of this class is to take a request for an item from a file, along with any sections it thinks the item might be in...
and return an array which contains [lineNum, numberOfLinesToSearchFor, lineNumToLookAtIfYouDon'tFindItThere, numberOfLinesToSearchFor, ...]
So that the actual finder only has to start at certain places and look for a certain amount of lines.

Right now, actually trying to use the sections is useless since my files are going to be pretty dang small.
So, I'm just going to convert any request into an array with [theInfoStartLineNumber, continueForever], whatever that turns out to look like.
'''
import HelpfulFunctions as hf
import FileFinderHelperMethods as ffhm

class FileFinderHelper0p0():
    def __init__(self, file, sectionSymbols):
        self.file = file #stores the file(name)
        self.update(True, sectionSymbols)

    def update(self, setInfoStartNow = False, sectionSymbols = None):
        def setInfoStart():
            #looks for a whitespace-stripped and lowercased line from the current cursor position that matches lookingFor.
            #if it can find it, it returns the line number
            #if it can't find it (it reaches the end of the file) then it returns None
            #sets the cursor to whatever line it finds.
            def findLineFromStart(theFile, lookingFor):
                '''
                upgrade: could find the character number and then I can just use seek to set the spot in the file more easily...
                But that also runs the risk of the file being changed. But so does finding the line number, which is what I'm doing now so...
                '''
                theFile.seek(0, 0)
                for lineNum, line in enumerate(theFile):
                    line = hf.completeStripAndLower(line)
                    if line==lookingFor: #found it
                        return lineNum
                return None #didn't find it
                
            with open(self.file) as f:
                infoStartLine = findLineFromStart(f, "infostart")
                if infoStartLine: #found it!
                    self.infoStartLine = infoStartLine
                    return
                else: #couldn't find the info start!
                    print("Warning! FileFinderHelper0p0: Could not find info start of file '{}'! Setting self.infoStartLine to the line after the format end.".format(f.name))
                    formatEndLine = findLineFromStart(f, "formatend")
                    if formatEndLine: #found at least a format end
                        self.infoStartLine = formatEndLine+1
                        return
                    else: #couldn't even find an end to the format!
                        print("Warning! FileFinderHelper0p0: Couldn't even find a format end in file '{}'! Setting self.infoStartLine to the first line.".format(f.name))
                        self.infoStartLine = 0
                        return
        #run
        if setInfoStartNow:
            setInfoStart()
        if sectionSymbols:
            self.sectionSymbols = sectionSymbols
    
    
    '''
    Let's pretend I did have a system up to use the sections efficiently.
    What would I want?
    
    I would first want the name of the thing I was asked to find.
    This is usually the lowest section.
    (In fact, they need two: the name of the item, and a symbol to surround items
    And that's necessary, right? Because anything lower is raw data, and the point is to st get the raw data.
    So for now, give me an array where the first item is the name (lowest section) of the thing to get.
    '''
    
    '''
    As a reminder, section symbols are in the form [item name symbols, item symbols, biggersection symbols, lessbiggersection symbols, ...]
    And here, capitalization and spacing matter.
    '''
    
    def run(self, findThis):
        #todo del
        import DebugHelper as dh
        def getToInfoStart(f, timesRun = 0): #f is the open file
            '''
                dh.log("where I'm at "+str(f.tell()))
                for lineNum, line in enumerate(f):
                    dh.log("where I'm at "+str(f.tell()))
                    if lineNum == self.infoStartLine:
                        if hf.completeStripAndLower(line)=="infostart":
                            dh.log("Caught the right line the first time!")
                            dh.log("here's what I got: "+str(f.tell()))
                            break
                        else:
                            self.update(True) #update the starting place since I didn't get it right.
                            f.seek(0, 0) #go back to the start of the file to find it again.
                            for corLineNum, corLine in enumerate(f):
                                if corLineNum == self.infoStartLine: 
                                    if hf.completeStripAndLower(corLine)=="infostart": #a quick second catch in case something really weird is going on.
                                        break
                                    else:
                                        print("Error: FileFinderHelper0p0: The infoStartLine keeps on being changed on me! I don't know how to function! Returning None.")
                                        return None
            '''
            
            for i in range(self.infoStartLine):
                f.readline()
            line = f.readline() #read one more time because range(x) goes up to x-1
            if hf.completeStripAndLower(line)=="infostart":
                return #found it and read past it. Should be right at the start of the information now
            else:
                if timesRun>1: #let it run through twice, then if it still can't get it right, stop it.
                    print("Error: FileFinderHelper0p0: The infoStartLine keeps on being changed on me! I don't know how to function! Returning None.")
                    return None
                self.update(True)
                self.update(True) #update the starting place since I didn't get it right.
                f.seek(0, 0) #go back to the start of the file to find it again.
                getToInfoStart(f, timesRun+1) #rerun this
                return #break out with nothing
                
        
        
        itemToFind = findThis[0]
        dh.log("info start line"+str(self.infoStartLine+1)) #human numbers
        with open(self.file) as f:
            getToInfoStart(f)
            #I am now at the start of the first info
            #I am now looking for the name of the item
            #goes to the character after the string is found
            #todo temp
            dh.log("character after 'infostart': {}".format(f.tell()))
            #todo find out why the next two parts are not working.
            ffhm.findStringFromCurrent(f, self.sectionSymbols[1]+itemToFind+self.sectionSymbols[2]) #todo del logs on its own
            #todo actually use this to return what it finds inbetween the symbols used to hold the item itself.
            dh.log("the section symbols")
            dh.log(self.sectionSymbols[4])
            dh.log(self.sectionSymbols[5])
            return ffhm.getInBetweenSymbolsFromCurrent(f, self.sectionSymbols[4], self.sectionSymbols[5])
            
def test():
    from DebugHelper import *
    import SymbolPageReader
    spr = SymbolPageReader.SymbolPageReader("Constants.txt")
    log("FINAL ANSWER:{}".format(spr.get("Input Level 0")))
    
test()