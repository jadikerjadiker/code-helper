'''
London Lowmanstone IV
Code Helper Class
Version 1.0
Before 10/30/2015
'''

import Tkinter as tk
import tkFileDialog as tkF
import tkMessageBox as tkM
import LDisplay as LD
import HelpfulFunctions as HF
'''
Notes:

Dictionary must include definition on how to use the word
The computer will know that it has a definition by excluding all the ^$ $^ stuff in the list part of the dictionary and just adding that to the def part
If the a word is caught at the front of a phrase, the definePhrase function will match the words and not try to define those separately.
Multiple definitions should not be supported yet.

Setup for word search:
Goes through and stores what is typed in as a list of words (right now they're just separated by space), called wordsToKnow.
Goes through each word and sees if it knows it; if the word is a part of phrase, it will check each word to see if that next word is the next word in the phrase until it gets to the end.
If the next word in the phrase is found, it marks the index of that word as found (MAKE SURE THAT WORDS THAT APPEAR IN DIFFERENT PHRASES AREN'T MARKED TWICE)
Then, when an entire phrase is completed, the words that were found are all deleted out of wordsToKnow (without shifitng down the other words)
If the phrase isn't found by the end

THIS ALSO DOES NOT DEAL WITH PHRASES THAT MAY BE EXTENDED VERSIONS OF OTHERS... This could be solved in the list by putting larger phrases in front of smaller phrases.
In other words, "set <<a>> to true if <<b>> is true" would come st before "set <<a>> to true" in the dictionary. (This has been solved, see notes below)

How to deal with a word that could be in more than one phrase... like "make <<a>> be equal to six" and "make the house and <<a>>...

First, the thing that gets the phrases must return all phrases that start with the word.
Then, each of those phrases is logged an given a number.
Then, each word is given an index in a table, where the numbers of all the phrases it could be a part of are logged in a table under that index (-1 means it can stand on its own).
Nothing happens until the computer is done looking through all the input.
The current tables are saved to be analyzed after definitions are gotten from the user (if needed)
Then, phrases that were not completely matched have their numbers taken out of all the tables.
Then, the longest matched phrase(the most words) is counted as matched to that phrase and logged as a phrase for the definer to work on(idk how rn)
Then, the next longest phrase checks to see if it can still complete itself, and if so, logs, all the way down to words that are self defined.

I have no idea how to deal with giving a definition to a phrase with words that have alread been logged as being in a phrase...
After the user defines each new phrase, the words in the phrase are checked to make sure they were catergorized as self-defined. 
If so, then assign the user-defined phrase a number and just assign those words to it.
If not, assign the user-defined phrase a number and then restart the looking for the longest phrase and matching. This will then update the words that definitions need to be asked for.
'''

class CodeHelper(tk.Frame):
    def __init__(self, parent):
        #todo set minimum width and height
        tk.Frame.__init__(self, parent, width=1, height=1)
        self.io = LD.SimpleInputOutputFrame(self)
        self.io.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    def removeActualCode(self, words):
        return words.replace("\s*<<.*?>>\s*", " ") #delete all code inside the ""<<"" ">>" marks and surrounding space and replaces it with one space

    def checkForDef(self, word): #checks to see if I know the word. This assumes the dictionary is static during the search. #todo make different dictionaries available. The first line says what dictionary type it is.
        with open("Dict") as Dict: #open the dictionary
            phrases = []
            foundList = False
            for line in Dict:
                if line=="*List:**": #found the start of the list of words with def's
                    foundList = True
                elif line=="*Definitions:**": #I've gotten to the end of the list (definitions are starting); word was not found
                    return False
                elif foundList:
                    if line==word: #the word is in the dictionary; return True
                        phrases.append(*SELF**)
                    elif line.startswith(word+" "):
                        phrases.append(line)
            return False #in case the dictionary has no definition marker (though it should have one)


    def getWordList(self, words):
        words = words.split() #split by spaces
        wordList = []
        for word in words:
            wordList.append(word)
        return wordList
'''
First, the thing that gets the phrases must return all phrases that start with the word.
Then, each of those phrases is logged an given a number.
Then, each word is given an index in a table, where the numbers of all the phrases it could be a part of are logged in a table under that index (-1 means it can stand on its own).
Nothing happens until the computer is done looking through all the input.
The current tables are saved to be analyzed after definitions are gotten from the user (if needed)
Then, phrases that were not completely matched have their numbers taken out of all the tables.
Then, the longest matched phrase(the most words) is counted as matched to that phrase and logged as a phrase for the definer to work on(idk how rn)
Then, the next longest phrase checks to see if it can still complete itself, and if so, logs, all the way down to words that are self defined.

I have no idea how to deal with giving a definition to a phrase with words that have alread been logged as being in a phrase...
After the user defines each new phrase, the words in the phrase are checked to make sure they were catergorized as self-defined. 
If so, then assign the user-defined phrase a number and just assign those words to it.
If not, assign the user-defined phrase a number and then restart the looking for the longest phrase and matching. This will then update the words that definitions need to be asked for.
'''
    def definePhrase(self, words) #matches each phrase to a definition in the dictionary. Uses a dictionary reader.
        dR = self.getDictReader()#sets dR to an object which will read the dictionary
        wordsToKnow = self.getWordList(words) #replaces everything inside the << >> with <<>> todo which will be defined as nothing, and returns a list of the words
                                              #(so straight code is still looked at as code, but is ignored)
        wordsKnown = [] #each index in this table corresponds to a tuple containing a word that has been looked at and the indexes of the phrases the word could be a part of
        possPhrases = [] #stores all the possible phrases that could be a part of the input
        phraseEnds = [] #stores the ends of phrases that have yet to be completed
        nextWords = [] #stores the next words in the phrases

        def chckPhraseMatches(keywordIndex): #returns the indexes of the phrases that were matched from nextWords (in a list) followed by the phrases that should be deleted (in a list) as a tuple
            keyword, myPhraseNums = wordsKnown[keywordIndex]
            matched = []
            delete = []

            def setupPossBlankMatchword(term): #if term starts with a blank, it sets blank to true (false otherwise) and returns the actual word, not the blank and the word 
                blank = False
                if term.startswith("^$$^ "): #see if a blank can be accepted
                            blank = True
                            term = term[5:] #cut down term to the actual word
                return term
                            
            if keyword=="<<>>": #if the word is code and not an actual word for a phrase
                for phraseNum, matchword in enumerate(nextWords):
                    #dp (short for delete print to remind myself to delete the print statement below)
                    print "chckPhraseMatches: count: "+str(count)+"matchword: "+matchword
                    matchword = setupPossBlankMatchword(matchword)
                    if not blank: #if the phrase was not expecting this, delete it
                        delete.append(phraseNum)
            else: #the word is a normal word and should be matched
                for phraseNum, matchword in enumerate(nextWords):
                    print "chckPhraseMatches: count: "+str(count)+"matchword: "+matchword                      
                    if matchword: #if there's an empty index it's just skipped
                        matchword = setupPossBlankMatchword(matchword)
                        if keyword==matchword: #match made!
                            matched.append(phraseNum)
                        else: #match failed!
                            if not blank: #if the phrase was not open to other words, delete it
                                delete.append(phraseNum)
            return matched, delete

                            
                            
 '''
#Helpful later on
if phraseNum in myPhraseNums: #If I have already listed myself as being a part of this phrase, there's something wrong with the definer
    print "Error! chckPhraseMatches: word '"+keyword+"' is already listed as being a part of the phrase '"+possPhrases[phraseNum]"'"
    return False #todo should this be "error" or False? Idk yet.
else:
    myPhraseNums.append(phraseNum)
    setupNextWordInPhrase(phraseNum) #todo write!
'''

        '''
        Here's how this works:
        Each word in the list of wordsToKnow will be looked at. The word <<>> will be mostly ignored, as that is straight code that does not need to be interpreted.
        It will still cause phrases expecting something else to be to be deleted though.
        When the definer looks at a word, it will first get a list of all phrases that it knows that start with that word
        Each one of those phrases will be added to possPhrases and assigned a number (their index in possPhrases) (todo it is unknown at this point whether or not this number will change, though it probably won't)
        and each phrase will be added to phraseEnds at the same index, and the first word in the phrase will be added to nextWords. If the first word is ^$$^ then the phrase added to nextWords is "^$$^"+(the second word)

        Then, the definer will look to see if the word matches any of the words in nextWords (if theres a ^$$^ then it matches the word directly after that (unless the current word is <<>> obviously)
        If it does match one, then the number of that phrase is stored under the word's index in wordsKnown, and the next word in the phrase is updated in nextWords (with the whole ^$$^ thing as described above) and phraseEnds is updated too.
        The tricky part is that if it doesnt match, then if theres a ^$$^, then it doesn't delete the phrase out of possPhrases, otherwise it does (and clears that index out of all the words in wordsKnown)
        
        After all this is done for all the words, it will check to see if there are any words it has no definition for (that are not a part of the phrase) and ask the user for definitions (that will probably result in a new phrasing alltogether.
        Any of the user-defined phrases should be added to the list of possPhrases and assigned to those words.

        If it has definitions for everything, then it will assign the actual phrases to the words based on the longest phrase and then check and delete any phrases that won't work.
        Repeat that process until there are no words with definitions left to define. Then, ask more questions and follow this process again if need be.
        If everything is defined, then return the possPhrase list and the wordsKnown list (as this will contain all the info to define the phrase)
        '''
                        
        
        for word in wordsToKnow:
            if word = "<<>>":
                
                
            else:
                
            
            


        
        '''
        wordsToKnow = self.getWordList(words)
        wordsKnown = []
        phraseParts = []
        wordsToLookFor = []
        for word in wordsToKnow:
            #first, check to see if this is a word you are looking for, and update the phrases you are looking for if it is
            if word in wordsToLookFor:
                indexes = HF.getAllIndexes(word, wordsToLookFor)

                
            knowWord = self.checkForDef(word)
            if isinstance(knowWord, str):
                phrases.append
'''
'''
        words = self.removeActualCode(words)
        for word in words.split() #assumes somthing is a word if and only if it is separated by space #todo change this to allow for space inside function parentheses
            knowWord = self.checkForDef(word)
            if isinstance(knowWord, str)
            if not self.checkForDef(word): #if the word is not defined yet, then ask the user to define it #todo write
                theDef = self.askForDef(word) #todo write!
                if not theDef: #If you don't give me a definition, I can't define the phrase...
                    return False
                self.storeDef(word, theDef) #todo write! #stores the word and definition in the dictionary file
        return True
'''
    
    def go(self, *args): #the heart of the helper: this converts your input into code
        myInput = self.io.inputT.get(1.0, "end") #get the input
        print("Your input:\n"+myInput+"End input.\n")
        self.io.inputT.delete(1.0, "end")
        phraseDefined = self.definePhrase(myInput) #make sure I have definitions for everything in the input
        if not phraseDefined:
            print("Could not define phrase!")
            return
        finalCode = self.convertIntoCode(myInput)#todo write! #take the input and turn it into code
        self.io.pOut(finalCode) #print out the code
        
