'''
London Lowmanstone IV
Simple CodeHelper Main.py
Version 1.00
1/7/2016
'''

import SymbolPageReader

#todo upgrade: stuff has to be added by hand to the text file.
#todo upgrade: patterns have to be added by hand
def main():
    toTranslate = raw_input("Input here:")
    print(translate(toTranslate))

def translate(string):
    def checkForPhrases(strs):
        for val in strs:
            spot = string.find(val)
            if spot!=-1:
                return spot, val
        return False, False #because it should return a tuple
        
    def checkForSpreadPhrase(parts, string = string):
        def isSorted(l):
            return all(l[i] <= l[i+1] for i in xrange(len(l)-1)) #from stackoverflow
                
        indexOfParts = []
        for i, part in enumerate(parts):
            place = string.find(part)
            if place==-1:
                return False #couldn't find a part
            else:
                #todo upgrade needs to at least check that the next part starts after the first part.
                indexOfParts.append(place) #todo upgrade: right now it just goes off of the first time it sees the words
        if isSorted(indexOfParts):
            return indexOfParts
        else:
            return False
            
            
        
    #run
    strsToLookFor = ["loop through array ", "for loop through ", "for through ", "fthru "]
    index, phrase = checkForPhrases(strsToLookFor)
    if not isinstance(index, bool): #bool is a subclass of int
        arrayName = string[index+len(phrase):]
        return "for (int i=0; i<"+arrayName+".length; ++i){\n\n}"; 
    
    indexes = checkForSpreadPhrase(["set ", " to "])
    if indexes:
        return string[indexes[0]+len("set "):indexes[1]]+" = "+string[indexes[1]+len(" to "):]

main()
