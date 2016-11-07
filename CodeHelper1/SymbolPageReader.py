'''
London Lowmanstone IV
SymbolPageReader Class
Version 2.7
11/30/2015
'''

'''
I'm basically rewriting this entire thing and just copying over stuff from the last one.
The goal of this one is to allow for a potentailly infinite amount of symbol levels.
So instead of having symbols to represent a "section" and then a "subsection" and then an "item"...
you declare the symbols in order from the biggest type of section to the smallest,...
and the symbols are stored in a list instead of individual variables.
'''

'''
Constructs with a page to read symbols from.
Right now it only reads symbol page format 0.0

The goal is to be able to return items quickly from a file by knowing what sections stuff is in.
But I can't find a way to make this useful for any short files right now,...
so I'm just going that part and just have it find the explicit values and I can todo update it later.

I will have to make sure that it accepts extra parameters to specify the sections and subsections the info is in...
but it won't use that information at all.

So it will have a part that it passes your request to, and then from that it just gets a starting place to look (since I know how to do that).
And, for now, that starting place will always be the start of the info. (Not the format stuff at the top)

The way that I want it to work is that when you ask for something in a certain section,...
it will then search the 
'''
import HelpfulFunctions as hf

class SymbolPageReader():
    def __init__(self, formatPage):
        self.DOES_CASE_MATTER = False #if true, it lowers everything before evaluating stuff.
        self.formatPage = formatPage
        def getFormatInfo():
            def getVersion(line):
                line = hf.completeStripAndLower(line)
                #print("returning with {}".format(line[line.find("version"):]))
                versionIndex = line.find("version")
                if versionIndex>=0:
                    return line[line.find("version")+7:]
                else:
                    return False
                
            
            with open(self.formatPage) as f: #open the page to read it
                self.pageVersion = getVersion(f.readline())
                if self.pageVersion=="0.0": #basically do a case check on the version
                    #load the module that gets the symbols from the page
                    import SectionSymbolFormat0p0Loader as sectSymLoader
                    self.sectionSymbolList = sectSymLoader.run(self.formatPage)
                    import FileFinderHelper0p0 as ffh
                    self.itemFinder = ffh.FileFinderHelper0p0(self.formatPage, self.sectionSymbolList)
                else:
                    print("SymbolPageReader:__init__:getFormatInfo:Error! Cannot read file with format number: {}".format(self.pageVersion))
        
        getFormatInfo()

    '''
    requestArray is in the form [nameOfItem, optional:typeNameOfSmallestSection, optional:smallestSectionToLookIn] (for now at least)
    or it can just be the string "nameOfItem"
    '''
    def get(self, requestArray):
        from DebugHelper import *
        if isinstance(requestArray, basestring): #if they use the string form, convert it to the array form.
            requestArray = [requestArray]
        if self.pageVersion=="0.0": #not sure if this sequence will need to be changed, but it doesn't hurt to have it.
            return self.itemFinder.run(requestArray)
        
        