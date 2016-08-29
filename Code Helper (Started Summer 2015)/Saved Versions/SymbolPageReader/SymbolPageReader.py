'''
London Lowmanstone IV
SymbolPageReader Class
Version 1.1 (redone to eliminate unused parameter)
10/31/2015 (11/1/2015)
'''

import HelpfulFunctions as hf

'''
I think the smarter way to program something like this...
where we literally have a list of things that are wanted and a name for each of the things is to
create two lists. The first one that holds all the actual values, and a second one that holds the human names.
So instead of self.SECTION_SYMBOL_INDICATOR we have
symbolIndicators = ["Section Symbol:", "Item Name Symbol:", "Item Symbol:"]
and
symbolIndicators_Names = ["SECTION_SYMBOL_INDICATOR", "ITEM_NAME_SYMBOL_INDICATOR", "ITEM_SYMBOL_INDICATOR"]
And then do
for index, name in enumerate(symbolIndicators_Names):
    setattr(self, name, symbolIndicators[index])
    
Then you can come up with better names, or even have the names stored in a doc somewhere or something like that.
But actually hard coding stuff in has to come at some point, and the reader is the place it has to start.
It's just a shame I made this first version so ugly.
'''


class SymbolPageReader():
    def __init__(self, formatPage):
        self.SECTION_SYMBOL_INDICATOR = "Section Symbol:"
        self.ITEM_NAME_SYMBOL_INDICATOR = "Item Name Symbol:"
        self.ITEM_SYMBOL_INDICATOR = "Item Symbol:"
        self.SECTION_REPLACEMENT = "Section"
        self.ITEM_NAME_REPLACEMENT =  "Item Name"
        self.ITEM_REPLACEMENT = "Item"
        self.DOES_CASE_MATTER = False #if true, it lowers everything before evaluating stuff.
        def getFormatInfo():
            ans = []
            for i in range(3): #create a table with three slots of lists;
            #each of the small lists should be filled with two pieces of info by the end
                ans.append([None, None])
            with open(self.formatPage) as f: #open the page to read it
                '''
                #testing
                if True:
                    for line in f:
                        print(line)
                    return True
                '''
                
                '''
                takes the string "Section Symbol:" or something like that that tells the computer
                you're about to tell it how to look for a new section.
                Also takes the thing inside of the sybol that stands in for the actual words, such as
                "Section" or "Item".
                Also takes the line it's supposed to find the info in 
                Assumes all parameters are lowercase.
                Returns the symbols that are supposed to go before the words and after the words as a tuple
                I know this sounds confusing, but if you just read through it, it will make sense.
                '''
                class quickSetUpSymbol():
                    #sets up the function
                    def __init__(self, line, ansTable, shouldLower):
                        self.shouldLower = shouldLower
                        self.line = line
                        if shouldLower:
                            self.line = self.line.lower()
                        self.ansTable = ansTable #will actually change the table
                    
                    #checkes to see if each answer in ans is not None
                    def isAnsFilled(self, theAns):
                        for val in theAns:
                            if val==[None, None]:
                                return False
                        return True
                    
                    #gets the before and after symbols for the given signal and returns them in a tuple (if found in the given line)
                    #returns False if it doesn't find the info
                    def findInfo(self, signal, insideSymbol, line):
                        #print("findInfo report: signal: {}\ninsideSymbol: {}\nline: {}".format(signal, insideSymbol, line))
                        where = line.find(signal)
                        if where==0:
                            pastSignal = len(signal) #saves the index that we need to start doing things just past the signal symbol
                            insideSymWhere = line.find(insideSymbol, pastSignal)
                            #print("insideSymWhere: {}".format(insideSymWhere))
                            #print("findInfo found info: {}".format((line[len(signal):insideSymWhere], line[insideSymWhere+len(insideSymbol):-1])))
                            #get the two respective pieces and return them.
                            #The -1 is there because there's a newline symbol at the end I don't want.
                            return (line[pastSignal:insideSymWhere], line[insideSymWhere+len(insideSymbol):-1]) 
                        else:
                            return False #no info in this line
                            
                    def setNewLine(self, line):
                        if self.shouldLower:
                            line = line.lower()
                        self.line = line
                        
                    def run(self, getThisInfo):
                        #getThisInfo is a list in the form [[symbolIndicator1, replaceSymbol1], [symbolIndicator2, replaceSymbol2], ...]
                        #lowering via code stuff that could be lowercased by hand (if it should be)
                        for pairNum, pair in enumerate(getThisInfo):
                            signal = pair[0]
                            insideReplacer = pair[1]
                            if self.shouldLower:
                                signal = signal.lower()
                                insideReplacer = insideReplacer.lower()
                            info = self.findInfo(signal, insideReplacer, self.line)
                            if info:
                                #print("info: {}".format(info))
                                ans[pairNum][0] = info[0]
                                ans[pairNum][1]= info[1]
                                #print("ans: {}".format(ans))
                        
                
                qSetUp = False #just declaring it for use
                for line in f:
                    #print("qSetUp type: {}".format(type(qSetUp)))
                    if not qSetUp:
                        qSetUp = quickSetUpSymbol(line, ans, self.DOES_CASE_MATTER) #it will lowercase the line
                    else:
                        qSetUp.setNewLine(line) #it will lower the line when it runs
                    qSetUpArgs = [] #set up the table that will contain what info we're looking for
                    qSetUpArgs.append([self.SECTION_SYMBOL_INDICATOR, self.SECTION_REPLACEMENT])
                    qSetUpArgs.append([self.ITEM_NAME_SYMBOL_INDICATOR, self.ITEM_NAME_REPLACEMENT])
                    qSetUpArgs.append([self.ITEM_SYMBOL_INDICATOR, self.ITEM_REPLACEMENT])
                    qSetUp.run(qSetUpArgs)
                    if qSetUp.isAnsFilled(ans):
                        print("ans is filled! Here's ans: {}".format(ans))
                        return ans
                print("SymbolPageReader:getFormatInfo(): Warning! Not all info found! I'm returning this as the symbols: {}".format(ans))
                return ans
        self.formatInfo = []
        self.formatPage = formatPage
        formatInfo = getFormatInfo() #should return [[beforeSectionSymbol, afterSectionSymbol], [beforeNameSym, afterNameSym], ..., ...]
        #print("returned formatInfo: {}".format(formatInfo))
        wantedInfo = ["sectionFormat", "itemNameFormat", "itemFormat"]
        hf.addNameAtts(self, wantedInfo, formatInfo)

#todo add the function that actually reads a value.
