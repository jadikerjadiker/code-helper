'''
London Lowmanstone IV
TellWhatsInside Class
Version 1.3
11/14/2015
Commenting
'''

#done in my normal model (as of 11/1/2015): the run() function does what the class is supposed to do, but there
#are other functions exposed as properties which could also be useful. The ones that aren't useful are
#defined inside run() so they are unaccessible from the outside.
class TellWhatsInside():
    '''
    nts: Overall, this class will probably need to be almost completely rewritten at some point,...
    as it does the very basics that I need it to do, and slowly at that.
    My main concern is ignoreable symbols, which are treated terribly, both in terms of time and flexibility.
    Right now the only one I need is "'"...
    (if "'" is included as an apostrophe inside a string, I don't want the class to search for a match to it)...
    so it's barely built to support that since I value getting it done right now over getting it done right.
    
    I hope that the way that I'm building this big system will allow for it to be upgraded instead of rewritten.
    I think that certain parts will be rewritten piece by piece as needed.
    '''
    def __init__(self):
        #define the big tables that are easier for a programmer to edit and change and understand
        #[symbol starting a parenthitcal section, ending symbol, another start, another end,...]
        #Rules:
        #All symbols are strings
        #no symbol con contain another symbol (ex: "_-_0_" and "_-_" does not work because "_-_" is in "_-_0_"
        #no two different ending symbols can have the same starting symbol. (ex: ["$^", "^$", "$^", "...$"] is not allowed for self.startsAndEnds) This can be easily changed in the function if need be.
        self.startsAndEnds = ["(", ")", "[", "]", "{", "}", '"', '"', "'", "'", "<il0>", "</>", "<il1>", "</>", "<il2>", "</>"]
        
        #[ignore this symbol, while you're inside this start, and this end]
        self.ignoreWhenInside = ["'", '"' , '"']

        #contains all the starts and ends, but removes the duplicates
        self.allSymbols = set(self.startsAndEnds)
        
        #nts: could make an alternate function here, but i think it's faster just to copy-paste the code right now.
        #now set up the littler tables that are easier for the program to use
        self.starts = []
        self.ends = []
        i = 0
        #goes through self.startsAndEnds and adds each symbol to the correct table.
        for val in self.startsAndEnds:
            if i == 0:
                self.starts.append(val)
                i = 1
            else:
                self.ends.append(val)
                i = 0
        
        self.canIngore = []
        self.ignorableContexts = []
        i = 0
        #goes through self.startsAndEnds and adds each symbol to the correct table.
        for val in self.ignoreWhenInside:
            if i == 0:
                self.canIngore.append(val)
                i = 1
            else:
                self.ignorableContexts.append(val)
                i = 0
    
    #Go through the entire string, tracking all the symbols and return all the paren. symbols used in a list (in order)
    def getAllSymbols(self, phrase, targetIndex):
        #print("getAllSymbols: recieved phrase {}".format(phrase))
        symAndPosTable = [] #stores the symbols and what position they appear at in the string
        for possSym in self.allSymbols:
            where = phrase.find(possSym, 0) #find it initially (if it's in the phrase)
            while(where!=-1): #as long as we keep on finding it in the phrase
                #print("getAllSymbols: found {} at index {}".format(possSym, where))
                symAndPosTable.append((possSym, where)) #add it and its position to the table
                where = phrase.find(possSym, where+len(possSym)) #setup the next search to start after the last spot where we found it
        symAndPosTable.append((None, targetIndex))
        def getKey(item):
            return item[1]
        symAndPosTable = sorted(symAndPosTable, key=getKey)
        ans = [symAndPos[0] for symAndPos in symAndPosTable]
        #dp
        print("getAllSymbols: returning {}".format(ans))
        return ans
    
    
    #compute what paren. expres. the target is in, given a list of all the symbols in the phrase (where None in the list is the target)
    def computeContext(self, theSymbols):
        ans =[]
        lookingForMatch = []
        targetMatch = []
        check = []
        hitTarget = False
        pastTarget = 0
        
        #nts: could be faster if it cached the values it had to look up previously in a dictionary instead of re-firguring it out every time.
        #gets ending symbol for a certain symbol. Returns None if the symbol is an ending symbol. Does not return anything 
        def getMatch(symbol):
            for index, val in enumerate(self.startsAndEnds):
                if val == symbol:
                    if index%2==0: #it's a starter
                        return self.startsAndEnds[index+1]
                    else: #it's an ender
                        return None
            #if symbol isn't recognized, print an error.
            print("getMatch: Error! Symbol: {} not recognized!".format(symbol))
        
        #prints a warning. Can take a symbol and index. Pretty self-explanatory.
        def printUnexpSymWarning(symbol = None, index = None):
            if symbol:
                if index:
                    print("computeContext: Warning! Extra symbol {} found in the phrase at index {}!".format(symbol, index))
                else:
                    print("computeContext: Warning! Extra symbol {} found in the phrase!".format(symbol))
            else:
                if index:
                    print("computeContext: Warning! Extra symbol found in the phrase at index {}!".format(index))
                else:
                    print("computeContext: Warning! Extra symbol found in the phrase!") 

        #returns False if the symbol can't be ignored, and True if it can.
        #toUpdate: this function is very slow and can be made faster (also can return more info that can be used later)
        def canSymBeIgnored(symbol):
            
            #takes a symbol and if it can be ignored, returns the paren. ex. that it can be ignored in. If not, returns False.
            def getIgnorableContext(symbol):
                for index, item in enumerate(self.ignoreWhenInside):
                    if item==symbol and index%3==0: #if it's the symbol given and it's not just a context
                        return [self.ignoreWhenInside[index+1], self.ignoreWhenInside[index+2]]
                    else:
                        return False
            
            #takes a list of symbols (where the target is None) and returns a new table where
            #the symbol at targetIndex is set to None and the original target is ignored.
            #this allows the context to be found for the symbol at targetIndex
            def setupSymTableForSymContext(initTable, targetIndex):
                ans = []
                for findIndex, val in enumerate(initTable):
                    if findIndex==targetIndex: #if it's the one that's supposed to be "None" then make it so.
                        ans.append(None)
                    elif val!=None: #skip over the None already in the symbol table.
                        ans.append(val)
                return ans
            
            #runner
            #Assumes that starting symbols are unique (no two ending symbols have the same starting symbol)
            iC = getIgnorableContext(symbol)
            if not iC: #if there's no context for it to be ignored in
                return False
            else:
                for toMatchSym in lookingForMatch:
                    if iC[0] == toMatchSym: #if it could be inside the paren. expression
                        currentContext = self.computeContext(setupSymTableForSymContext(theSymbols, indexNum))
                        if (iC[0]+iC[1]) in currentContext: #if the symbol can actually be ignored we're fine.
                            return True
                        else: #the symbol isn't in the correct context
                            return False
                #gone through all symbols in lookingForMatch and none of them are the starter for its ignore context: it can't be ignored
                return False
            
        #runner
        for indexNum, symbol in enumerate(theSymbols):
            if symbol == None: #hit the target
                #print("Computecontext: Hit target at: {}".format(indexNum))
                hitTarget = True
                if len(lookingForMatch)==0: #there aren't any more symbols to match
                    return ans
            else:
                #print("Got to symbol {}".format(symbol))
                if not canSymBeIgnored(symbol):
                    if targetMatch and symbol == targetMatch[-1]: #this is the ender we're looking for
                        #print("It's the correct ender")
                        if hitTarget and pastTarget == 0: #if the paren. ex. encompasses the target.
                            ans.append(lookingForMatch[-1]+symbol)
                        lookingForMatch.pop()
                        targetMatch.pop()
                        if hitTarget and len(lookingForMatch)==0: #if we've passed the target and there's nothing left to match
                            return ans #we're done, return the answer
                        if pastTarget > 0: #if we matched one that started past the target, lower pastTarget by 1.
                            pastTarget-=1
                    else:
                        match = getMatch(symbol) #see if this symbol is a starter by returning its ender if it has one, or None if it doesn't
                        if match!=None: #it is a starter
                            #print("It's a starter")
                            #add itself and its match to the lists
                            lookingForMatch.append(symbol)
                            targetMatch.append(match)
                            #if this starter is past the target, then increment pastTarget by 1
                            if hitTarget:
                                pastTarget+=1
                        else: #this can't be ignored and it's not a starter or ender - print a warning
                            printUnexpSymWarning(symbol, indexNum)
        if len(lookingForMatch)!=0: #if there's starters that haven't been matched yet
            for symbol in lookingForMatch: #print a warning for each of them.
                printUnexpSymWarning(symbol)
        return ans #return the answer.
            
    def run(self, phrase, index):
        '''
        #Testing!!!
        def test():
            print(self.getAllSymbols("hello everone's cows there {(world) how are }you", 15))
        
        if True:
            test()
            return
        
        
        #Testing!!!
        '''
        
        
        #the first character in the string can't be in a parenthetical statement, so if that's what I'm told to check, I'm done.
        if index==0:
            return []
        else:
            #compute what paren. expres. the target is in, given a list of all the symbols in the phrase (where None in the list is the target)
            return self.computeContext(self.getAllSymbols(phrase, index))


def test():
    t = TellWhatsInside()
    print(t.run("<il0>{he"+'"'+"llo (wor'ld)"+'"}'+" </>", 13))
    
test()
