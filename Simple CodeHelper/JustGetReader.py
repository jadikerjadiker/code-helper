'''
London Lowmanstone IV
JustGetReader Module
Version 1.4
2/19/2016
'''

'''
Gets the value of an item from a format file.
'''
#ONLY WORKS WITH A NON-AMBIGUOUS SYMBOL AFTER THE ITEM
#Technically not an actual reader as it does not take into account the starts and endings of sections.
#So, if an item contains something that looks like it could be another item, this will interpret it as that other item.
#In other words, USING THIS CAN CAUSE ERRORS

#itemName is the name of the item in the file to return the value of
#file is the unopened file
#fileInfo is in the form
#[
#    [
#        [before item name, inbetween item name and item, after item], 
#        [before the smallest section title, after the smallest section title, between elements, after elements are done],
#        [before the second smallest section title, after the second smallest section title, between elements, after elements are done],
#        ...etc
#    ],
#    [item, item name, smallest section title, second smallest section title]
#]

import string

def run(itemName, file, fileInfo):
    #reads the info from the file from cursor up until the target
    #caseMatters should be set to True if the target needs to be case-sensitive
    #readThrough should be true if it should leave the cursor at the index after the target. Otherwise, it will set the cursor to be right before the target.
    def readInfo(target, save = True, caseMatters = True, readThrough = True, delInfoNewline = False):
        if target == "": #if there's an empty string for a target, just return an empty string
            return ""
        if not caseMatters:
            target = target.lower() #in case target wasn't already lowercased
        checkr = "" #short for "check read": it's a substring of lr that is being checked for the target
        fr = "" #short for "final read" which contains the string in the original case and eventually will only contain the string in between the start and target
        targetlen = len(target) #cache
        
        b = f.read(1) #read one byte from the file
        while b!="": #as long as I haven't hit the end of the file
            if save: #save what's been read
                fr+=b
            if caseMatters:
                checkr+=b
            else:
                checkr+=b.lower()
            while True:
                checkrlen = len(checkr) #cache
                if string.find(checkr, target[:len(checkr)])!=-1 or checkrlen==0: #if checkr is a match thus far or is empty
                    if targetlen==checkrlen: #if we've matched the entire target
                        if not readThrough: #if I'm not supposed to read through the target, jump the cursor back to right before the target
                            f.seek(-targetlen, 1)
                        if save: #if there is something that should be returned
                            if delInfoNewline:
                                return dealWithNewline(fr[:-targetlen]) #return what was found inbetween and deal with the extra newline if there's non-newline info in it
                            else:
                                return fr[:-targetlen] #return what was found inbetween
                        else:
                            return
                    break
                else:
                    checkr = checkr[1:] #take off the first character and see if it can then start a new match
            b = f.read(1)
        raise IOError("Format1p0Loader.run(): reached the end of the file before reading '{}'".format(target))
    
    #run
    with open(file) as f:
        inInfo = fileInfo[0][0] #short for "item name info" #cache
        readInfo("\n"+inInfo[0]+itemName+inInfo[1], save = False) #get up to the info
        return readInfo(inInfo[2])
        