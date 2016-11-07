'''
London Lowmanstone IV
SectionSymbolFormat0p0Loader Module
Version 3.1
12/14/2015

Changed formatend to endformat
'''

'''
Section symbol finder for format 0.0:
Tell it to run and give it an unopened file and it will return the table of symbols...
needed to recognize sections and subsections in the order they were written.
'''
'''
The table returned (if it runs successfully) will be in the form:
[section type name, symbol to left of title, symbol to right of title, ...repeating]
where the first item in the list is how the names of items will be signaled...
and the second item in the list is how the items themselves will be signaled...
and then after that it goes biggest subsection to smallest subsection.

This is due to how the person is supposed to create 
'''
import HelpfulFunctions as hf

def run(unopenedFile):
    with open(unopenedFile) as file:
        ans = []
        for lineNum, line in enumerate(file):
            '''
            The line should be in the form
            "Item name symbol: ### Item name ###"
            So that when the computer sees something like...
            "### Item #23 ###" it knows that that is an item with the name "Item #23"
            
            So more formally the line is in the form:
            
            (section name) symbol:(symbol before)(section name)(symbol after)
            
            Where (section name) can be anything; it's really only for human readability (I call it a placeholder), ...
            and (symbol before) and (symbol after) are the symbols the computer looks for...
            to identify an object at that section level, and "symbol:" is exactly as written.
            '''
            if lineNum>0: #if it's not the version line
                line=line.strip()
                line = line.lower() #I don't care about case
                if line!="": #if the line is not just empty space
                    if hf.completeStrip(line)=="endformat":
                        ansLen = len(ans)
                        if ansLen<6: #if they didn't give me everything I need
                            print("Warning! SectionSymbolFormat0p0Loader: Did not recieve name and item symbols correctly. Returning array as is.")
                            if ansLen%3!=0: #woah, something is really wrong. The array's not even in the right format!
                                print("Error! SectionSymbolFormat0p0Loader: Array has incorrect amount of items (incorrect format)! Returning it as is.")
                        return ans
                    '''
                    I just decided to not allow space in between the word "symbol" and the colon because...
                    I didn't want to have to import and use regex...
                    So that may be changed later on.
                    '''
                    BREAKER = " symbol:" #what we're looking for inbetween the section name and the symbols
                    sectionName = hf.getSubstringInBetween(line, False, BREAKER)
                    if sectionName==None:
                        print("Warning! SectionSymbolFormat0p0Loader: Did not find the correct format at line {}. Returning the symbols I got.".format(lineNum+1))
                        return ans
                    leftSymbol = hf.getSubstringInBetween(line, BREAKER, sectionName)
                    rightSymbol = hf.getSubstringInBetween(line, sectionName, False, line.find(BREAKER))
                    if sectionName!=None and leftSymbol!=None and rightSymbol!=None: #if this is supposed to be a symbol definition
                        ans.append(sectionName)
                        ans.append(leftSymbol)
                        ans.append(rightSymbol)
                    else:
                        print("Warning! SectionSymbolFormat0p0Loader: Suspected bad format at line {}. I skipped that line.".format(lineNum+1))
        print("Error! SectionSymbolFormat0p0Loader: encountered EOF before format end! Returning the symbols I got.")
        return ans