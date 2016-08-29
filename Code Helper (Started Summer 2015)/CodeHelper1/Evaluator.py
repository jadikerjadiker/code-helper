'''
London Lowmanstone IV
Evaluator Class
Version 2.1
11/16/2015
'''

import TellWhatsInside as contextGetter

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

class Evaluator():
    def __init__(self):
        SYMBOL_FILE = "inputLevelSymbols.txt"
        self.symbolReader
        self.sectionSymbolArrays = 
    
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
        def getIL(string):
            contextGetter.TellWhatsInside(SYMBOL_FILE)
            
        
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
