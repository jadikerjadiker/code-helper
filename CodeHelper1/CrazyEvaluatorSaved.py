'''
This is very recursive. Basically this thing searches for anything that's not basic, and plugs it into itself.
Then, it takes the basic stuff that comes out and returns it.

The evaluator is going to get a string that either starts with an IL or
it assumes the IL is 1 (metacode).

If it's IL 0 then:
search the inside for anything that's inside an IL 1 indicator.
Evaluate what's inside and then replug it back in.
If it's all IL 0 then just return the evaluation.

If it's IL 1:
Evaluate anything that's not a string.
Now that it's just one funtion that manipulates strings:
Get the definition, plug in the strings for the variables, and return the evaluated new string.
'''
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
        self.startsAndEnds = ["(", ")", "[", "]", "{", "}", '"', '"', "'", "'", "_-_0_", "_-_", "_-_1_", "_-_", "_-_2_", "_-_"]
        #[ignore it if you only see one of this symbol, while you're inside this symbol]
        self.ignoreWhenInside = ["'", '"' , '"']
        
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
        c = 0
        ans = []
        phraseLen = len(phrase)
        if phraseLen==0: #if you don't give me a string, I'm just going to return two empty tables and tell you that you didn't give me anything.
            print("getAllSymbols: WARNING! Empty string given as phrase!") 
            return []
        
        while c<phraseLen:
            if c==targetIndex:
                ans.append(None) #assumes that None is not a possible symbol to be parenthetical start of end
            else:
                curSym = phrase[c]
                if curSym in self.startsAndEnds: #if the symbol is a paren. symbol, then add it to the table.
                    ans.append(curSym)
            c+=1
        #dp
        print("getAllSymbols is returning: {}".format(ans))
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
        
        #takes a symbol and if it can be ignored, returns the paren. ex. that it can be ignored in. If not, returns False.
        def getIgnorableContext(symbol):
            for index, item in enumerate(self.ignoreWhenInside):
                if item==symbol and index%3==0: #if it's the symbol given and it's not just a context
                    return [self.ignoreWhenInside[index+1], self.ignoreWhenInside[index+2]]
                else:
                    return False #todo are empty tables False or True? I'm guessing True.
        
        #prints a warning given a symbol. Pretty self-explanatory
        def printUnexpSymWarning(sym):
            print("computeContext: ERROR! Extra symbol {} found in the phrase that does not belong!".format(sym))
            
        def setupSymTableForSymContext(initTable, targetIndex):
            ans = []
            for findIndex, val in enumerate(initTable):
                if findIndex==targetIndex: #if it's the one that's supposed to be "None" then make it so.
                    ans.append(None)
                elif val!=None: #skip over the None already in the symbol table.
                    ans.append(val)
            return ans
        '''
        So, to recap:
        First, check to see if the symbol can be ignored period.
        If it can't, print a warningd
        If it can be ignored, then check to see if any of the symbols waiting to be matched are the starting symbol of...
        the context that it can be ignored in.
        If not, then it won't be in that context, and do the error and return ans thing. (nts: this can be removed)
        If it could be in the context, then run this function on the list of symbols to find out what its context is.
        If the context contains the peren. ex. that allows it to be ignored, then ignore it! Otherwise, don't.
        
        Nts: I have to make sure that the symbol is included on these recursive runs so that getAllSymbols doesn't...
        print out an error due to an empty string.
        
        What if instead of causing an error, it just printed a warning and then assumed the symbol wasn't supposed to be there...
        and moved on.
        
        That's what it's going to do. Actually creating an error does me no good since now it will either (1) tells me something's wrong with the program or...
        (2) tell the user that they entered something wrong, versus completely stopping them.
        
        Plus, if I need it to be a legit error, I can just change the function later.
        '''        
        #prints a warning and returns false if the symbol shouldn't be there. Returns true otherwise.
        def dealWithUnexpectedSym(symbol):
            #todo write test function and then do if True: test() return to actually run it without the compiler getting mad.
            #Assumes that starting symbols are unique (no two ending symbols have the same starting symbol)
            iC = getIgnorableContext(symbol)
            if not iC:
                printUnexpSymWarning(symbol)
                return False
            else:
                for toMatchSym in lookingForMatch:
                    if iC[0] == toMatchSym: #if it could be inside the paren. expression
                        currentContext = self.computeContext(setupSymTableForSymContext(theSymbols, indexNum))
                        if (iC[0]+iC[1]) in currentContext: #if the symbol can actually be ignored we're fine.
                            return True
                        else:
                            printUnexpSymWarning(symbol)
                            return False
                #gone through all symbols in lookingForMatch and none of them match: print a warning.
                printUnexpSymWarning(symbol)
                return False
    
        def canSymBeIgnored(symbol):
            #todo write test function and then do if True: test() return to actually run it without the compiler getting mad.
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
            
            
        '''
        the goal is to figure out which paren. expressions go across the gap.
        I am going to do this by starting with the first symbol, and going across.
        If I get to another opener, I start looking for a match to that instead.
        If this opener is past the target, I increment pastTarget by one.
        If I get a closer that matches, I check to see if I've crossed the gap and that pastTarget==0.
        If so, then tack that paren. pair onto the ans table and then check to see if there are any more left to match.
            If there is nothing left to match then I'm done and I can just return it.
        If the closer doesn't match, then I check to see if it's something I can ignore.
        If I can ignore it, I check to make sure it's in the correct ignorableContext
        If I can't ignore it, I just print a warning.
        
        Also, when I hit the gap, I check to see if I have any symbols left to check for matches.
        If not, then I'm done. (Since there's no paren. that could contain the target since it doesn't start before the target)
        '''
        '''
        #TESTING!!!
        def test():
            lookingForMatch 
            print("Testing dealWithUnexpectedSym")
            print("Using } and just running it with that. It should just print an error")
            dealWithUnexpectedSym("}")
            
        if True:
            test()
            return
        #TESTING!!!
        '''
        
        '''
        Okay, I'm rethinking this.
        Now I think the logic is going to go like this:
        
        If (it's the target):
            set hitTarget to True and return if you're done.
        Else:
            If (the symbol can't be ignored): #don't print an error yet if it can't
                if (it's a starter):
                    add it to lookingForMatch
                    add its match to targetMatch
                    if (you're past the target):
                        increment pastTarget by 1
                elif (it's an ender):
                    if (the match spans over the target):
                        add the starter+ender to the answer
                    take it and its starter off the end of the targetMatch and lookingForMatch tables
                    if we're done: (this is similar to code above, but is pointless to put into a function.
                        return ans
                    If pastTarget >0:
                        pastTarget-=1
                else:
                    print a warning
        '''
        for indexNum, symbol in enumerate(theSymbols):
            if symbol == None: #hit the target
                #dp
                print("Computecontext: Hit target at: {}".format(indexNum))
                hitTarget = True
                if len(lookingForMatch)==0: #there aren't any more symbols to match
                    return ans
            else:
                symIgnoreInfo = canSymBeIgnored()
                if not symIgnoreInfo:
                    match = getMatch(symbol)
                    if #todo finish
        '''
        for indexNum, symbol in enumerate(theSymbols):
            if symbol == None: #hit the target
                print("Computecontext: Hit target at: {}".format(indexNum))
                hitTarget = True
                if len(lookingForMatch)==0: #any more symbols to match?
                    return ans #nope, I'm done.
            else: #this is a symbol
                #dp
                print("Computecontext: Hit symbol: {}".format(symbol))
                if targetMatch and symbol == targetMatch[-1]: #this is the match for the one we're looking for
                    #dp
                    print("It's the correct ender")
                    if hitTarget and pastTarget == 0: #if the paren. ex. encompasses the target.
                        ans.append(lookingForMatch[-1]+symbol)
                    lookingForMatch.pop()
                    targetMatch.pop()
                    if pastTarget > 0:
                        pastTarget-=1
                else: #either it's a starter or something we're not expecting
                    match = getMatch(symbol)
                    if match!=None: #if this is a starter
                        #dp
                        print("It's a starter")
                        #add itself and its match to the lists
                        lookingForMatch.append(symbol)
                        targetMatch.append(match)
                        #if this starter is past the target, then increment pastTarget by 1
                        if hitTarget:
                            pastTarget+=1
                    else: #I wasn't expecting this ending symbol
                        del\'''
                        Here's how I'm going to deal with this.
                        First, check to see if the symbol can be ignored period.
                        If it can't, print an error and return the current ans table in hope that might work better
                        If it can be ignored, then check to see if any of the symbols waiting to be matched are the starting symbol of...
                        the context that it can be ignored in.
                        If not, then it won't be in that context, and do the error and return ans thing.
                        If so, then literally ignore it;
                        (if that starter is matched, then it's inside an ignoreable context...
                        and if it's never matched, then that brings up an error anyways!
                        ...unless it was ignoreable. In which case I have to rethink this.
                        
                        Also, should some things only be ignoreable when their most recent shell is the context?
                        like if "i" is ignoreable when in "{}", then could we have it so that it's not ignored in "{(i)}"...
                        since it's not directly in the "{}" ("{}" is not its outer shell)?
                        
                        So interestingly, the goal seems to be to find out what the symbol is inside...
                        which is what this function is trying to do!
                        So maybe I can make it recursive. The issue though is that I don't want to be losing information...
                        since when it re-runs it it will probably gather some info about how the symbols are organized that will be
                        recalculated later.
                        
                        So should I literally make it recursive now? Or spend more time and try to make it faster?
                        I'm just going to make it recursive for now and then I can spend time later making it faster.
                        todo: could be made faster by either not making it recursive or by having...
                        the recursive call to the function return more info.
                        
                        Right now I'm also just going to have it deal where if the context is surrounding it anywhere...
                        it's considered to be in that context.
                        del\'''
                        #deals with an unexpected symbol. If it should ignore it, it does nothing.
                        #If the symbol shouldn't be there, it just prints an error.
                        #dp
                        print("wasn't expecting this symbol! Can it be ignored?")
                        dealWithUnexpectedSym(symbol)
        return ans
        '''
            
            
            
            
        '''            
        #----------------------Redoing some stuff here----------------------------------
                #dp
                print("Computecontext: Hit symbol: {}".format(symbol))
                match = getMatch(symbol)
                if match!=None: #if this is a starter
                    #dp
                    print("It's a starter")
                    #add itself and its match to the lists
                    lookingForMatch.append(symbol)
                    targetMatch.append(match)
                    #if this starter is past the target, then increment pastTarget by 1
                    if hitTarget:
                        pastTarget+=1
                else:
                    if symbol == targetMatch[-1]: #this is the match for the one we're looking for
                        #dp
                        print("It's the correct ender")
                        if hitTarget and pastTarget == 0: #if the paren. ex. encompasses the target.
                            ans.append(lookingForMatch[-1]+symbol)
                        lookingForMatch.pop()
                        targetMatch.pop()
                        if pastTarget > 0:
                            pastTarget-=1
                    else: #I wasn't expecting this ending symbol
                        del\'''
                        Here's how I'm going to deal with this.
                        First, check to see if the symbol can be ignored period.
                        If it can't, print an error and return the current ans table in hope that might work better
                        If it can be ignored, then check to see if any of the symbols waiting to be matched are the starting symbol of...
                        the context that it can be ignored in.
                        If not, then it won't be in that context, and do the error and return ans thing.
                        If so, then literally ignore it;
                        (if that starter is matched, then it's inside an ignoreable context...
                        and if it's never matched, then that brings up an error anyways!
                        ...unless it was ignoreable. In which case I have to rethink this.
                        
                        Also, should some things only be ignoreable when their most recent shell is the context?
                        like if "i" is ignoreable when in "{}", then could we have it so that it's not ignored in "{(i)}"...
                        since it's not directly in the "{}" ("{}" is not its outer shell)?
                        
                        So interestingly, the goal seems to be to find out what the symbol is inside...
                        which is what this function is trying to do!
                        So maybe I can make it recursive. The issue though is that I don't want to be losing information...
                        since when it re-runs it it will probably gather some info about how the symbols are organized that will be
                        recalculated later.
                        
                        So should I literally make it recursive now? Or spend more time and try to make it faster?
                        I'm just going to make it recursive for now and then I can spend time later making it faster.
                        todo: could be made faster by either not making it recursive or by having...
                        the recursive call to the function return more info.
                        
                        Right now I'm also just going to have it deal where if the context is surrounding it anywhere...
                        it's considered to be in that context.
                        del\'''
                        #deals with an unexpected symbol. If it should ignore it, it does nothing.
                        #If the symbol shouldn't be there, it just prints an error.
                        #dp
                        print("wasn't expecting this symbol! Can it be ignored?")
                        dealWithUnexpectedSym(symbol)
        return ans 
        
        #---------------------------------redoing stuff is over--------------------------------------
        '''

   
    
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
                
            
            
            
        
class Evaluator():
    def __init__(self):
        def setup():
            def setupIndicators():
                def calcIndicatorStartForIL(num):
                    return self.IND_S.replace("val", num)
                self.IND_S = "_-_val_"
                self.IND_E = "_-_"
                self.IL1_IND = "1"
                self.IL2_IND = "2"
                self.IL1_IND_S = calcIndicatorStartForIL("1")
                self.IL2_IND_S = calcIndicatorStartForIL("2")
                
            setupIndicators()

            
        setup()
    
    '''    
    IND_S = "_-_val_"
    IND_E = "_-_"
    def calcIndicatorStartForIL(num):
        return IND_S.replace("val", num)
    IL1_IND = "1"
    IL2_IND = "2"
    IND1_IND_S = calcIndicatorStartForIL("1")
    IND2_IND_S = calcIndicatorStartForIL("2")
    '''
    
    def evaluate(self, toEval): #runs the code passed in as a string called toEval
        
        il = getIL(toEval) #todo write!
        if not(il==0 or il==1):
            print("Evaluator: Error! Got input level: {} (should be 1 or 0)".format(il))
        
        '''
        If it's IL 0 then:
        search the inside for anything that's inside an IL 1 indicator.
        Evaluate what's inside and then replug it back in.
        If it's all IL 0 then just return the evaluation.
        '''
        #just to be clear, toEval is a string, but strings inside of toEval are not searched.
        if il == 0:
            '''
            So when I say "inside an IL1 indicator", what do I mean?
            The only thing I need to check for is that it's not inside another string.
            Other than that I can just replace it with the evaluated text.
            It doesn't matter where it is in any parenthetical situation
            (like _-_0_ _-_1_ stuff _-_ _-_) since it's meant to be evaluated anyways...
            and if it's on the outside, the evaluator will just get to the one on the inside...
            and if it's on the inside, the evaluator will find the one on the outside.
            
            So I want a regex that will match any INDICATOR up through the matching _-_ ender.
            It also needs to understand all other indicators and enders so it knows to ignore them.
            And ignore anything inside a string (which means to also keep track of anything that could signify a string inside of the string)
            
            It might be better to do this programatically instead of with a gigantic regex that's impossible to read/understand later.
            So that's what I'm going to do.
            '''
            '''
            The basic method is to first search for _-_1_ and if I don't find any, just evaluate it.
            If I do find one, use a multi-purpose function that will just tell me what brackets and/or other stuff the...
            indicator is inside of.
            
            For example if the string is "hello 'testing {_-_1_ stuff _-_ something}' hi []"
            The function will return ["{}", "''"] since it's first inside {} and then inside '' (and then it's just inside the string, which is a given)
            The function will also recognize that if the closing symbols don't appear or appear in the wrong order that it's not a match.
            '''
            
            
            
        
        
    '''
    First, I need to scan for the outside stuff and keep going inside until I get to a base layer which is a string.
    '''
def test():
    t = TellWhatsInside()
    testing = '"'+"there's something that should be ignored"+'"'
    print(t.run(testing, 5))
    #t.computeContext(["(", "@", None, ")"])

test()