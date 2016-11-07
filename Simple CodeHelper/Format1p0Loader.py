'''
London Lowmanstone IV
Format1p0Loader Module
Version 6.0
2/17/2016

5.x -> 6.x: Made it so that you can type stuff before the format.
'''

import string

#the goal of this is to return with an array containing all the info about spacing for the different sections in a format 1.0 file

'''
What it returns should be in the form:
[
    [
        [before item name, inbetween item name and item, after item], 
        [before the smallest section title, after the smallest section title, between elements, after elements are done],
        [before the second smallest section title, after the second smallest section title, between elements, after elements are done],
        ...etc
    ],
    [item, item name, smallest section title, second smallest section title]
]
'''

#returns the info described above. file is a closed text file.
def run(file):
    #cut the trailing newline off of a string (if there is one)
    def cutTrail(string):
        if string[-1:]=="\n":
            return string[:-1]
        return string
    
    '''
    When you have information in between two lines, generally if there is no information, you have something like:
    line1
    line2
    which is the same as 'line1\nline2'
    and the info is ''
    
    But then if the information is just a newline you have:
    line1
    
    line2
    which is the same as 'line1\n\nline2'
    and the info is '\n'
    
    But then if you have information that's not just a newline you do:
    line1
    abc
    line2
    which is the same as 'line1\nabc\nline2'
    but the info is 'abc', not '\nabc' or 'abc\n'.
    
    So if there's information other than just newlines, this function cuts off the trailing newline so that the information can be gotten correctly.
    Note that generally a previous function reads past the first \n so that one is assumed to be already cut off.
    '''
    #cuts off the trailing newline if there is something other than newlines in the string
    def dealWithNewline(string):
        for char in string:
            if char!="\n":
                return cutTrail(string)
        return string
    
    #reads until it hits a non-space character. If save is True it stores and then returns what it read.
    #EOF is a non-space character, so it should never go into an infinite loop
    def readUntilNonSpace(save = False):
        ans = ""
        while True:
            val = f.read(1)
            if not(val=="\n" or val=="\t" or val==" "): #will return if True
                if val!="": #if I didn't just reach the end of the file
                    f.seek(-1, 1) #go to the byte before
                if save:
                    return ans
                else:
                    return
            if save: #saves what has been read
                ans+=val
    
    #reads one line and cuts off the trailing newline. Raises an exception if the cursor is at the end of the file    
    def readNonEndLine():
        line = f.readline()
        if line=="":
            raise IOError("Format1p0Loader.run():readNonEndLine(): should not have found end of file")
        else:
            return cutTrail(line) #take off the trailing newline
    
    #reads the info from the file from cursor up until the target
    #caseMatters should be set to True if the target needs to be case-sensitive
    #readThrough should be true if it should leave the cursor at the index after the target. Otherwise, it will set the cursor to be right before the target.
    def readInfo(target, caseMatters = False, readThrough = True, delInfoNewline = True):
        if target == "": #if there's an empty string for a target, just return an empty string
            return ""
        if not caseMatters:
            target = target.lower() #in case target wasn't already lowercased
        checkr = "" #short for "check read": it's a substring of lr that is being checked for the target
        fr = "" #short for "final read" which contains the string in the original case and eventually will only contain the string in between the start and target
        targetlen = len(target) #cache
        
        b = f.read(1) #read one byte from the file
        while b!="": #as long as I haven't hit the end of the file
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
                        if delInfoNewline:
                            return dealWithNewline(fr[:-targetlen]) #return what was found inbetween and deal with the extra newline if there's non-newline info in it
                        else:
                            return fr[:-targetlen] #return what was found inbetween
                    break
                else:
                    checkr = checkr[1:] #take off the first character and see if it can then start a new match
            b = f.read(1)
        raise IOError("Format1p0Loader.run():readInfo():reached the end of the file before reading '{}'".format(target))
    
    #listOfStringAndCases is in the form [(string to read up to, boolean does case matter), (next string, next boolean) etc.]
    #it will read the info (and dispose of unneeded newlines if needed) up to all the strings in listOfStringAndCAses concatenated,
    #making sure the case matches if necessary.
    #assumes that listOfStringAndCases does not have any '\n' characters in it
    #automatically reads through
    #automatically deals with an extra newline in the info
    def readCasedInfoLine(listOfStringsAndCases, delInfoNewline = True):
        #makeError is defined below so that it can use bigtarget
        bigtarget = "" #the concatenation of all the strings
        for val in listOfStringsAndCases:
                bigtarget+=val[0]
        bigtargetLen = len(bigtarget) #cache
                
        def makeError():
            raise IOError("Format1p0Loader.run(): hit end of file while looking for '{}'".format(bigtarget))
            
        ans = ""
        f.seek(-1, 1)#move back one character
        #read until a newline, storing what is read (removing the first character that was backtracked)
        while True:
            val = f.read(1)
            if val=="":
                makeError()
            ans+=val
            if val=="\n":
                break
        ans = ans[1:] #cut off that first backtracked character
        while True: #look for the ending
            try:
                line = readNonEndLine()
            except IOError: #revise the error message to be more specific
                makeError()
                
            if len(line) == bigtargetLen: #if it even has a chance of being the correct line
                start = 0
                for i, v in enumerate(listOfStringsAndCases):
                    string = v[0] #cache
                    
                    if v[1]: #case matters
                        check = (line[start:start+len(string)]==string)
                    else: #case doesn't matter
                        check = (line[start:start+len(string)].lower()==string.lower())
                     
                    if check: #if it matches thus far   
                        stop = start+len(string) #where the string should stop inside the line #cache
                        if i==len(listOfStringsAndCases)-1:
                            if delInfoNewline:
                                return dealWithNewline(ans) #found what we wanted
                            else:
                                return ans
                        else:
                            start = stop #the next start should be where this one stopped
                    else:
                        #note that if this actually gets to the end of a file (where the '\n' should not be appended)
                        #then the next readNonEndLine() will raise an error anyway
                        #so we shouldn't worry about what ans is at that point (since it won't be returned)
                        
                        print('broke')
                        break #get a new line to run through
            ans+=line+'\n' #should return if the for loop were actually to run through
    
    #run    
    with open(file) as f:
        f.readline() #skip over the first line that says the format
        #I'm forgetting which version of the line reading I can use.
        #sets up ans with the correct amount of inner tables
        ans = [[], []]
        info = ans[0]
        humanNames = ans[1] #what the programmer called the different sections
        #setup the section hierarchy
        readCasedInfoLine([("start format", False)])
        readUntilNonSpace()
        line = readNonEndLine()
        #todo upgrade: make sure none of the names are equal to eachother
        while line!="":
            humanNames.insert(0, line) #put the name it into the human names part of the answer
            info.append([]) #give it a slot for info in the part that really matters in the answer, the info for fomatting.
            line = readNonEndLine()
        
        info.pop() #since the info for the item and item name are combined
        
        #set up everything but the item name and item info
        for i in range(len(info)-1):
            currentSlot = info[-i-1] #cache
            currentName = humanNames[-i-1] #cache
            #read in a section
            readUntilNonSpace()
            
            #check name line
            title = readNonEndLine()
            #upgrade if the titles are not equal, it could ask the user which one it wants to use and then replace it.
            if title!=currentName+":":
                raise IOError("Format1p0Loader.run(): section info heading '{}' does not match the expected '{}'".format(title, currentName+":"))
            
            #check example line
            if readNonEndLine().lower()!='example:': #readNonEndLine() consumes the newline, but does not store it
                raise IOError("Format1p0Loader.run(): was expecting 'example:' but instead got '{}'".format(exampleLine))
                
            #read the example
            titleStuff = readInfo("between elements:\n") 
            whereToPut = string.find(titleStuff, currentName)
            if whereToPut == -1:
                raise IOError("Format1p0Loader.run(): expected to find '{}' within the example".format(currentName))
            currentSlot.append(titleStuff[:whereToPut]) #store what should go before the title
            currentSlot.append(titleStuff[whereToPut+len(currentName):]) #store what should go after the title
            
            betweenStuff = readInfo("after:\n") #read what needs to be in between elements of the section
            currentSlot.append(betweenStuff)
            
            #read what should go after all the elements
            afterStuff = readCasedInfoLine([(currentName, True), (" done", False)])
            currentSlot.append(afterStuff)
            
        #store the info for the item and item name
        currentSlot = info[0]
        humanItem = humanNames[0] #what the human calls the item #cache
        humanItemName = humanNames[1] #what the human calls the item name #cache
        lenhumanItemName = len(humanItemName) #cache
        lenhumanItem = len(humanItem) #cache 
         
        readUntilNonSpace()
        title = readNonEndLine()
        #make sure it's the correct header. It should be in the form 'humanItemName and humanItem:'.
        if title[:lenhumanItemName]!=humanItemName or title[lenhumanItemName:lenhumanItemName+5].lower()!=" and " or title[lenhumanItemName+5:]!=humanItem+":":
            raise IOError("Format1p0Loader.run(): section info heading '{}' does not match the expected '{}'".format(title, humanItemName+" and "+humanItem+":"))
        
        #check example line
        if readNonEndLine().lower()!='example:':
            raise IOError("Format1p0Loader.run(): was expecting 'example:' but instead got '{}'".format(exampleLine))
        
        #add the item name and item info to the list
        currentSlot.append(readInfo(humanItemName, delInfoNewline = False)) #get and store the symbols in front of the item name
        currentSlot.append(readInfo(humanItem, delInfoNewline = False)) #get and store the symbols in between the item name and the item
        #get and store the symbols after the item name and the item
        #Note that here we are reading from the end of a line instead of the start of a new one
        #so we need to not deal with the newline (because then if our info is just newlines dealWithNewline() won't cut it off)
        #but instead cut the trailing newline for sure with cutTrail().
        currentSlot.append(cutTrail(readCasedInfoLine([(humanItemName, True), (" and ", False), (humanItem, True), (" done", False)], delInfoNewline = False)))
        readCasedInfoLine([("format done", False)])
        return ans