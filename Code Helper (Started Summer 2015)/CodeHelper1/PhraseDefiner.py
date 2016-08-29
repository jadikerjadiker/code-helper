import re
import copy
import HelpfulFunctions as HF
'''
Notes:
The phrase definer has one main function that assigns phrases (and later on certain definitions)
to the string of words inputed into it.
It returns a tuple of two tables:

The first is a table of the phrases (/definitions), where the index of the phrase is that phrases "number"

The second is a table containing a tuple of each "word" in the phrase (any straight code is turned into the word "<<>>")
and the number of the phrase (/definition) it's associated with. Code ("<<>>") is not associated with anything,
so that table will be empty.
'''


class PhraseDefiner:
    def __init__(self, helper):
        self.helper = helper
        self.nextWordRegEx = "(?:\^\$\$\^ )?.*?(?:\s|$)+" #matches a word and and the blank (^$$^) before it (only if the blank is there) and the space after it

    '''
    definePhrase:

    Assigns words in a phrase to phrases that are already defined

    Here's how this works:
    Each word in the list of wordsToKnow will be looked at. The word <<>> will be mostly ignored, as that is straight code that does not need to be interpreted.
    It will still cause phrases expecting something else to be to be deleted though.
    When the definer looks at a word, it will first get a list of all phrases that it knows that start with that word
    Each one of those phrases will be added to possPhrases and assigned a number (their index in possPhrases)
    and each phrase will be added to phraseEnds at the same index, and the first word in the phrase will be added to nextWords. If the first word is ^$$^ then the phrase added to nextWords is "^$$^"+(the second word)

    Then, the definer will look to see if the word matches any of the words in nextWords (if theres a ^$$^ then it matches the word directly after that (unless the current word is <<>> obviously)
    If it does match one, then the number of that phrase is stored under the word's index in wordsKnown, and the next word in the phrase is updated in nextWords (with the whole ^$$^ thing as described above) and phraseEnds is updated too.
    The tricky part is that if it doesnt match, then if theres a ^$$^, then it doesn't delete the phrase out of possPhrases, otherwise it does (and clears that index out of all the words in wordsKnown)

    After all this is done for all the words, it will check to see if there are any words it has no definition for (that are not a part of the phrase) and ask the user for definitions (that will probably result in a new phrasing alltogether.
    Any of the user-defined phrases should be added to the list of possPhrases and assigned to those words.

    If it has definitions for everything, then it will assign the actual phrases to the words based on the longest phrase and then check and delete any phrases that won't work.
    Repeat that process until there are no words with definitions left to define. Then, ask more questions and follow this process again if need be.
    If everything is defined, then return the possPhrase list and the wordsKnown list (as this will contain all the info to define the phrase)

    During the matching process, I need to watch out for phrases that are the same that have both been matched up to the same number word:
    If that happens, only the most recent one should match the end phrase, and if only one ends up finishing, a question needs to be posed.

    After the matching process, the rule is longest (in terms of words) first, and then the one that came up first, first.

    Currently Fails When:
    You meant the two shorter phrases to be separate, not the longer one that's them combined
    You use a phrase that it's expecting after a blank inside a blank
    The combination of one shorter phrase following another shorter phrase and it uses the longer phrase that it finds in the middle of those two
    Unsure about newLines failing, but high likeliness 

    Basic Idea:
    possPhrases, phraseEnds, and nextWords are a lists of strings (that should always contain the same amount of entries)
    wordsToKnow is a list of tuples where each tuple contains (word, list of numbers of phrases this word could be a part of)
    possPhrases holds all of the phrases that are possible to exist inside the given text to convert
    phraseEnds holds the parts of these phrases that have not been matched yet
    nextWords holds the next word that the phrase needs to match
    wordsToKnow holds the words in the text to convert and what phrases they could be a part of

    todo (not in order of importance):
    1. It would be smarter to change it so that the phrases that have been matched are moved to another list that is never looked at when matching.
    This would make it much faster to match so that it doesn't always iterate over things that are done.

    1.2 It would be smarter to also move the deleted phrases out...

    2. Change error messages so that they actually throw personalized errors

    3. Should be rewritten with just one function instead of an object... The methods of this object are practically useless to anything else

    4. So it turns out that lists can be modified in functions... Delete all the crazy return stuff! And the crazy equal settings!
    (everything I'm currently writing is still going to use the unneeded stuff for consistency (and sanity) sake.
    BEWARE ANYTHING THAT USES A LIST TO DETERMINE ANOTHER VALUE!

    todok:
    1. make wordsToKnow into an object with methods such as addMatchToWord(wordNum, 5) etc.
    The most useful method rn would be deleteAllPhraseMatchesOf(phraseNum) and it would just delete them.
    also wouldn't have to keep on passing it as a parameter it could just do this stuff on its own.



    Terms I use:
    straight code: Code that does not need to be edited: it could be run straight in the normal GUI for that language
    high code: Code that the helper uses to determine how to translate a phrase
    normal code: code written for the helper to translate.
    nts: note to self - other people may not be able to understand it which is fine because it's just a note to myself.
    '''

###NEEDED FOR definePhrase ###
    def takeOutNumFromWordList(self, num, wordsToKnow): #takes the phrase with number num out of any word that was matched to it
        #dp
        printOut("takeOutNumFromWordList: num, wordsToKnow: ", (num, wordsToKnow)) #debug
        for aTuple in wordsToKnow:
            word, indexes = aTuple
            while True: #this should actually only be done once for each
                try: #this is faster than a "while num in indexes" (for small and large amounts of matches) and an "if num in indexes" (for large amounds of matches)
                    indexes.remove(num)
                except:
                    break
            #printOut("takeOutNumFromWordList: check to make sure I got the number out.", wordsToKnow)#debug
        return wordsToKnow
    
    def getWordList(self, words):
        words = re.sub("<<.*?>>", "<<>>", words).split() #split by spaces and turn straight code into ""<<>>""
        wordList = []
        for word in words:
            wordList.append(word)
        return wordList

    def setup_wordsToKnow(self, phrase):
        wordsToKnow = self.getWordList(phrase)
        for index, word in enumerate(wordsToKnow):
            wordsToKnow[index] = (word, [])
        return wordsToKnow
            
        

    #uses the dictionary translator (dT) to add all the phrases to possPhrases (puts the phrases (without the first word) in phraseEnds and the next word in nextWords as expected)
    #that start with the word "word"
    #Returns a tuple: (possPhrases, phraseEnds, nextWords) updated, of course
    #Right now, if there is no next word, next word becomes '' instead of None or empty.
    def addPhrases(self, dT, wordIndex, wordsToKnow, possPhrases, phraseEnds, nextWords):
        ###DEFINITIONS###
        def getNextWordAndPhrase(phrase): #returns a tuple of the second word in the phrase and the phrase with the first word cut out
            phraseEnd = re.sub(self.nextWordRegEx, "", phrase, count=1) #gets rid of the first word (and any one ^$$^ at the front)
            #print("getNextWordAndPhrase: Phrase end:"+phraseEnd)
            nextWord = re.match(self.nextWordRegEx, phraseEnd).group(0).strip()
            #print("getNextWordAndPhrase: nextWord:"+nextWord)
            return nextWord, phraseEnd
        ###DEFINITIONS END###

        word, phraseNums = wordsToKnow[wordIndex]             
        phrasesToAdd = dT.getPSW(word) #todo write! #short for "getPhrasesStartingWith"
        for phrase in phrasesToAdd:
            if not HF.allEqual(len(possPhrases), len(phraseEnds), len(nextWords)): #this shouldn't happen, but I want to display a warning if it does.
                print("addPhrases: ERROR! The phrase lists are not all the same size!")
            possPhrases.append(phrase)
            #dp stuff
            if len(possPhrases)-1 >13:
                printOut("addPhrases: CAUGHT SOMETHING FISHY! number (top index of possPhrases) then possPhrases", len(possPhrases)-1, possPhrases)
            phraseNums.append(len(possPhrases)-1)
            nextWord, remainingPhrase = getNextWordAndPhrase(phrase)
            phraseEnds.append(remainingPhrase)
            nextWords.append(nextWord)
        #todo delete this: nts: so something is happening in between this and getPhraseMatchOrder so that possPhrases is losing some elements 
        #dp
        printOut("This is the possPhrases that I'm giving back", possPhrases, "Top index:", len(possPhrases)-1)
        return possPhrases, phraseEnds, nextWords


    def emptyOutPhrase(self, num, wordsToKnow, possPhrases, phraseEnds, nextWords):
            possPhrases[num] = ""
            phraseEnds[num] = ""
            nextWords[num] = ""
            wordsToKnow = self.takeOutNumFromWordList(num, wordsToKnow)
            return wordsToKnow, possPhrases, phraseEnds, nextWords             

    #deletes the incompleted phrases (phrases with non-blank words in phraseEnds) from all three lists and removes those numbers from words in wordsToKnow
    #returns the four lists as a tuple: wordsToKnow, possPhrases, phraseEnds, nextWords
    def deleteIncompletePhrases(self, wordsToKnow, possPhrases, phraseEnds, nextWords):
        def phraseIsEmpty(phrase): #returns False if the phrase has something else to match. #todok this can be upgraded to a better regex instead of an "if"
            if phrase==None or phrase=="" or phrase == "^$$^":
                return True
            else:
                return False

        #dp
        print("deleteIncompletePhrases: started")
        for phraseNum, phrase in enumerate(phraseEnds):
            #todo delete the stuff below
            #dp stuff
            #if phraseNum == 15:
                #printOut("15 alert!!! here's wordsToKnow, possPhrases, phraseEnds, nextWords, and phraseIsEmpty", wordsToKnow, possPhrases, phraseEnds, nextWords, phraseIsEmpty(phrase)) 
            
            if not phraseIsEmpty(phrase): #if there was something left to match
                #dp
                printOut("deleteIncompletePhrases: deleting number "+str(phraseNum)) #debug
                wordsToKnow, possPhrases, phraseEnds, nextWords = self.emptyOutPhrase(phraseNum, wordsToKnow, possPhrases, phraseEnds, nextWords)
        return wordsToKnow, possPhrases, phraseEnds, nextWords
                




    #does the final matchup between the phrases remaining and the words, and asks questions as needed to clarify (may even ask to redefine the phrase)
    '''
Rules:
User-defined phrases take precedence
Matches the longest phrase first, and if there's a tie, goes by the first phrase in the list.
Asks questions if any words are undefined after this.

Failures described in class descriptor

Final matches will be returned as a tuple of two lists: [phrase one, phrase two, phrasethree, ...], [(word, phraseNum), (word, phraseNum), ...]
    '''
    def finalMatchup(self, wordsToKnow, possPhrases, orig = []):
        
        def getPhraseMatchOrder(wordsToKnow, possPhrases):
            #origList holds the original values of [wordsToKnow, possPhrases, phraseMatchOrder]
            def getLengthOfPhrase(index, possPhrases): #counts how many words (excluding blanks) are in the phrase whose phrase number is index
                #todo finish this is returning an index error
                return len(re.findall(self.nextWordRegEx, possPhrases[index]))

            #returns what slot a phrase with length phraseLength should be stored within lengthList
            def getStorageSlot(phraseLength, lengthList):
                for i, compLength in enumerate(lengthList):
                    if phraseLength > compLength: #if there's a tie, this phrase came later so it will move down
                        return i
                return "add" #returns "add" if it should append it to the end of the list

            ans = [] #what's going to be returned; the first index is the phrase that will be matched first and so on.
            length = [] #length[i] is the length (in words) of the phrase at ans[i]. This is used to make sure that longer phrases take top precedence
            #first seen takes precedence, so this will match down the line starting with the first seen phrases so that ties can automatically be added later.
            #dp
            printOut("getPhraseMatchOrder: wordsToKnow", wordsToKnow)
            printOut("getPhraseMatchOrder: possPhrases", possPhrases)
            printOut("getPhraseMatchOrder: len(possPhrases)", len(possPhrases))
            for wordTuple in wordsToKnow:
                word, phraseNums = wordTuple
                for index in phraseNums:
                    if not index in ans: #If I haven't already figured out where this should go in the list
                        phraseLength = getLengthOfPhrase(index, possPhrases)
                        place = getStorageSlot(phraseLength, length)
                        if place=="add":
                            length.append(phraseLength)
                            ans.append(index)
                        else:
                            length.insert(place, phraseLength)
                            ans.insert(place, index)
            return ans

        def matchPhrase(num, wordsToKnow, possPhrases, wordsKnown, phraseMatchOrder):
            def matchWordToPhrase(wordIndex, phraseNum, wordsKnown):
                if type(wordsKnown[wordIndex])==tuple: #if the word has already been matched
                    print("matchWordToPhrase: ERROR! Word has already been matched!")
                    #printOut("here's the index and wordsKnown", wordIndex, wordsKnown)
                    #printOut("And the part that I'm measuring the length of:", list(wordsKnown[wordIndex]))
                #Goes on assuming that it hasn't already been matched    
                word = wordsKnown[wordIndex]
                wordsKnown[wordIndex] = (word, phraseNum)
                return wordsKnown

            #deletes the used phrase and any now unusable phrases from the phraseMatchOrder list.
            def deleteBrokenPhrases(nums, phraseMatchOrder):
                #assumes that the number is only in the phraseMatchOrder once
                for num in nums:
                    try:
                        phraseMatchOrder.remove(num)
                    except:
                        pass
                return phraseMatchOrder
                    
            for wordIndex, wordTuple in enumerate(wordsToKnow): #iterates through every word in wordsToKnow and sees if that word is a part of the phrase
                word, phraseNums = wordTuple
                for index in phraseNums:
                    if index==num: #if it is, then match the word to the phrase, finally
                        wordsKnown = matchWordToPhrase(wordIndex, num, wordsKnown)
                        phraseMatchOrder = deleteBrokenPhrases(phraseNums, phraseMatchOrder)
                        break #it doesn't need to go through any of the other numbers
            return wordsKnown, phraseMatchOrder
                        

        def setup_wordsKnown(wordsToKnow):
            wordsKnown = []
            for wordTuple in wordsToKnow:
                word, phraseNums = wordTuple
                wordsKnown.append(word)
            return wordsKnown
            
        #temp (for testing)
        def getDefinitionsForUnknowns():
            pass
            
        #this is finalMatchup
        phraseMatchOrder = getPhraseMatchOrder(wordsToKnow, possPhrases)
        if not orig:
            orig = [copy.deepcopy(wordsToKnow), copy.deepcopy(possPhrases), copy.deepcopy(phraseMatchOrder)] #need this to stay the same no matter what happens to the other lists

        wordsKnown = setup_wordsKnown(wordsToKnow) #create a new list that will store the final matches. (Easier than deleting the unused matches from wordsToKnow)

        while True:
            try:
                curPhraseNum = phraseMatchOrder[0]
            except:
                break
            #adds the phrase index to the correct words in wordsKnown and deletes the phrase indexes off of phraseMatchOrder that are no longer completeable due to the match
            wordsKnown, phraseMatchOrder = matchPhrase(curPhraseNum, wordsToKnow, possPhrases, wordsKnown, phraseMatchOrder)
        getDefinitionsForUnknowns() #gets definitions from the user and rematches stuff. This is there origWordsToKnow comes in handy. #todo write!
        #nts: could work just by adding the userdefined phrases to the top of the old list; the words aren't going to change.
        return possPhrases, wordsKnown


    #takes two list in the following form: [(word, phraseNum), (word, phraseNum), ...], [phrase, phrase, phrase, ...]
    #the first list is usually wordsKnown, and the second one is usually possPhrases
    #cleans up the final matchup by deleting the unused phrases and making the numbers go straight up from 0
    def cleanupFinalMatchup(self, wordList, phraseList):
        #makes a list of all the phrase numbers matched by words (unsorted)
        def getUsedPhraseNums(wordList):
            #todok could be more effective, but I'm assuming not a lot of phrases are going to be used
            #so there's not much of a reason to find a better way than using "in"
            ans = []
            for wordTuple in wordList:
                word, num = wordTuple
                if not num in ans:
                    ans.append(num)
            #print("Used phrase nums: ", ans)
            return ans
                    
        #creates a list of how many numbers are in-between each of the numbers in numList (looks at -1 and the first number in numList first)
        def getNumsInMiddle(numList):
            ans = []
            ans.append(numList[0]) #amount of times to delete index 0 until the first number in numList becomes item 0
            for i in range(len(numList)-1):
                ans.append(numList[i+1]-numList[i]-1)
            #print("getNumsInMiddle: got numList of ", numList, "and returning ", ans)
            return ans

        #todo upgrade should not have to make another entire list, should just use the index as the new number.
        #makes a key where the old number is listed right before the new number
        def makeKeyList(numList):
            ans = []
            for new, old in enumerate(numList):
                ans.append(old)
                ans.append(new)
            #print("Key list: ", ans)
            return ans

        #uses the key to get the new number
        def getNewNum(old, key):
            #search through the list to find the old key, the number at the next index is the new key; return it
            #assumes key has an even number of entries
            #print("looking for number: "+str(old))
            for i in range(len(key)/2):
                index = i*2
                #print("looking @ index: "+str(index))
                if key[index]==old:
                    return key[index+1]

            print("getNewNum: Error! New key not found...")
            return None #this will probably throw an error somewhere down the line sooner than returning a number (todo change comment if exception is actually raised)

            
        numList = getUsedPhraseNums(wordList)
        numList.sort()
        #gets how many numbers are in between each of the numbers in the sorted numList so that it will delete that many times to get the numbers to be straight in order.
        delTimes = getNumsInMiddle(numList)
        curInd = 0
        for delNum in delTimes: #deletes all the phrases in between the used phrases.
            for i in range(delNum):
                phraseList.pop(curInd) #deletes phrases until the next used phrase
            curInd+=1 #moves onto the next space to start deleting (this won't throw an error at the end since delTimes will have ended and stopped the loop)
        for i in range(len(phraseList)-curInd): #delete all the ones at the end
            phraseList.pop(curInd)
        keyList = makeKeyList(numList) #keyList is [oldNum, newNum, oldNum, newNum, ...]
        #print("wordsToKnow: ",wordsToKnow)
        for index, wordAndIndexes in enumerate(wordList):
            word, phraseNum = wordAndIndexes
            #print("index: ", index, "word and phraseNum", word, phraseNum)
            wordList[index] = word, getNewNum(phraseNum, keyList) #substitutes the new number for the old one.
        return wordList, phraseList
            
            
        

    #matches the word found at wordsToKnow[wordIndex] to phrases in possPhrases and updates the lists.
    #This includes deleting unneeded phrases from all lists (and all words in wordsToKnow)
    #Returns a tuple: (wordsToKnow, possPhrases, phraseEnds, nextWords) (all updated)
    #todo delete
    #wordsToKnow, possPhrases, phraseEnds, nextWords = self.matchToPhrases(wordNum, wordsToKnow, possPhrases, phraseEnds, nextWords)
    def matchToPhrases(self, wordIndex, wordsToKnow, possPhrases, phraseEnds, nextWords):
        #takes the index/number of the word in wordsToKnow, and the two lists, wordsToKnow and nextWords
        #returns the indexes of the phrases that were matched from nextWords (in a list) followed by the phrases that should be deleted (in a list) as a tuple
        def checkPhraseMatches(word, nextWords):
            def setupPossBlankMatchword(term, blank): #if term can accept a blank, blank is set to true. Then, if there's another word to match afterwards it sets term to be just that word. Returns term.
                blank = False
                if term.startswith("^$$^"): #see if a blank can be accepted
                    blank = True
                    if term.startswith("^$$^ "): #if there's another word afterwards to match
                        term = term[5:] #cut down term to the actual word
                return term, blank

            matched = []
            delete = []
            blank = False
            if word=="<<>>": #if the word is code and not an actual word for a phrase
                for phraseNum, matchword in enumerate(nextWords):
                    #print "chckPhraseMatches: phraseNum: "+str(phraseNum)+" matchword: "+matchword
                    matchword, blank = setupPossBlankMatchword(matchword, blank)
                    if not blank: #if the phrase was not expecting this, delete it
                        delete.append(phraseNum)
            else: #the word is a normal word and should be matched
                for phraseNum, matchword in enumerate(nextWords): #go through every next word in the phrases
                    #print "chckPhraseMatches: phraseNum: "+str(phraseNum)+" matchword: "+matchword                      
                    if matchword: #if there's an empty index it's just skipped (empty includes an empty string)
                        matchword, blank = setupPossBlankMatchword(matchword, blank)
                        if not matchword=="^$$^": #because ^$$^ will just accept anything
                            if word==matchword: #match made!
                                matched.append(phraseNum)
                            else: #match failed!
                                if not blank: #if the phrase was not open to other words, delete it
                                    delete.append(phraseNum)
            return matched, delete

        #sets nextWords[num] to the next word and phraseEnds[num] to the rest of the phrase.
        #similar to getNextWordAndPhrase(), but different enough that I wanted them separate.
        def updateRemainingPhrase(num, phraseEnds, nextWords):
            #print(phraseEnds[num])
            phraseEnds[num] = re.sub(self.nextWordRegEx, "", phraseEnds[num], count=1)
            nextWords[num] = re.match(self.nextWordRegEx, phraseEnds[num]).group(0).strip()
            #print("to: "+str(phraseEnds[num]))
            return phraseEnds, nextWords

        #this is matchToPhrases
        #nts: first, match a word, then update the ones that need to be updated and delete the ones that need to be deleted. Then return. Mission accomplished, wizard!
        #printOut("wordIndex", wordIndex,"wordsToKnow", wordsToKnow,"possPhrases", possPhrases, "phraseEnds", phraseEnds,"nextWords", nextWords) #debug
        #dp
        printOut("About to match wordNum "+str(wordIndex)+"! Here's wordsToKnow, possPhrases, phraseEnds, and nextWords", wordsToKnow, possPhrases, phraseEnds, nextWords)
        word, phraseNums = wordsToKnow[wordIndex]
        if len(phraseNums)>0:
            print("matchToPhrases: WARNING! Word already has some phrases it is matched to. Shouldn't hurt anything though, just odd.")
        toUpdate, toDelete = checkPhraseMatches(word, nextWords)
        for phraseNum in toUpdate:
            phraseEnds, nextWords = updateRemainingPhrase(phraseNum, phraseEnds, nextWords) #updates phraseEnds and nextWords to show the next word
            phraseNums.append(phraseNum) #phraseNums may or may not have anything in it already, I just ignore what's in there; it shouldn't hurt anything down the line
        for phraseNum in toDelete:
            wordsToKnow, possPhrases, phraseEnds, nextWords = self.emptyOutPhrase(phraseNum, wordsToKnow, possPhrases, phraseEnds, nextWords) #different than delete phrase since it won't actually delete the phrase, just make all entries empty strings
            #does not delete the phrases since that would mess up the indexes/phrase numbers of the phrases ahead of it; the matcher (checkPhraseMatches) automatically skips over empty strings
            #print("Emptied out: "+str(phraseNum))
        return wordsToKnow, possPhrases, phraseEnds, nextWords


    def setupDictTranslator(self):
        class fakeDictTrans: #fake dictionary for testing
            def __init__(self):
                pass

            def getPSW(self, word): #fake version of the getPSW method (short for "getPhrasesStartingWith")
                if word=="make":
                    return ["^$$^ make ^$$^", "make my day", "make ^$$^", "make something useless", "make ^$$^ please", "^$$^ make me happy", "make my day please", "make ^$$^ please"]
                elif word=="my":
                    return ["my house", "my day", "my ^$$^", "my ^$$^ world"]
                elif word=="day":
                    return ["day - oh!", "day please", "^$$^ day"]
                elif word=="please":
                    return["^$$^ please", "please work everytime for everything because that would be wonderful"]
                else:
                    print("fakeDictTrans: ERROR! Word: "+str(word)+" is unknown by the dictionary!")
                    return []
        return fakeDictTrans()
    
    #todo ignoring the fancy check for two of the same phrases for now - DONT START TWO OF THE SAME PHRASES BEFORE ENDING THEM
    #local functions and vars are used only when defining another phrase would interfere with those variables or functions
    def definePhrase(self, phrase): #defines a phrase as described in the notes
        #todok delete all the variables that are unneeded by the end
        curPhrase = phrase
        dictTranslator = self.setupDictTranslator() #todo write! #sets up the dictionary readers for whatever dictionaries are needed to look through.
        wordsToKnow = self.setup_wordsToKnow(curPhrase)
        possPhrases = []
        phraseEnds = []
        nextWords = []
        for wordNum, wordTuple in enumerate(wordsToKnow):
            word, indexes = wordTuple
            if not wordNum==0: #there aren't any phrases to match if it's the first word
                #matches the word to any of the phrases in possPhrases and updates the tables
                wordsToKnow, possPhrases, phraseEnds, nextWords = self.matchToPhrases(wordNum, wordsToKnow, possPhrases, phraseEnds, nextWords)
                print("definePhrase: Phrases matched! wordNum is "+str(wordNum))
                print(wordsToKnow)
            #adds all of the phrases that start with the word and automatically matches the word to the added phrase
            possPhrases, phraseEnds, nextWords = self.addPhrases(dictTranslator, wordNum, wordsToKnow, possPhrases, phraseEnds, nextWords)
        #deletes the phrases that were never completed
        wordsToKnow, possPhrases, phraseEnds, nextWords = self.deleteIncompletePhrases(wordsToKnow, possPhrases, phraseEnds, nextWords)
        #gives the final numbers of the matchup to the words
        #dp
        printOut("Right before final matchup!!!! Here's wordsToKnow, possPhrases")
        finalPhrases, finalMatches = self.finalMatchup(wordsToKnow, possPhrases)
        #dp
        printOut("Basically done, just making it simpler! Here's finalPhrases, finalMatches", finalPhrases, finalMatches)
        #deletes all the extra spaces in possPhrases and changes the numbers of the indicies in wordsToKnow
        finalMatches, finalPhrases = self.cleanupFinalMatchup(finalMatches, finalPhrases) #todo check
        return finalMatches, finalPhrases

def printOut(*args):
    for item in args:
        print(item)
    print("\n")

def test(testNum):
    def printOut(*args):
        for thing in args:
            print thing
            print "\n"
    if testNum == 1: #test matchToPhrases and cleanupFinalMatchup
        wordsToKnow = [("make", [6]), ("my", []), ("day", [6]), ("please", [6])]
        possPhrases = ["make my program", "make everything", "make me a cake", "make my day please", "make ^$$^", "^$$^ make ^$$^", "make my ^$$^", "make ^$$^ my friend", "make my ^$$^ man look happy"]
        phraseEnds = ["my program", "everything", "me a cake", "my day please", "^$$^", "^$$^", "my ^$$^", "^$$^ my friend", "my ^$$^ man happy"]
        nextWords = ["my", "everything", "me", "my", "^$$^", "^$$^", "my", "^$$^ my", "my"]

        pd = PhraseDefiner(2)
        wordsToKnow, possPhrases, phraseEnds, nextWords = pd.matchToPhrases(1, wordsToKnow, possPhrases, phraseEnds, nextWords)
        printOut(wordsToKnow, possPhrases, phraseEnds, nextWords)
        wordsToKnow[1] = ("my", [3])

        wordsToKnow, possPhrases = pd.cleanupFinalMatchup(wordsToKnow, possPhrases)

        print("after cleanup")

        printOut(wordsToKnow, possPhrases)
    elif testNum == 2: #test finalMatchup
        pd = PhraseDefiner(2) #any number to substitute as the helper XD

#todo delete tests
#test(1)

def finalTest(testNum):
    if testNum==1:
        pd = PhraseDefiner(2)
        answer, phrases = pd.definePhrase("make my day please")
        print('ANSWER!!')
        print(answer)
        print('PHRASES!!')
        print(phrases)
    if testNum==2:
        pd = PhraseDefiner(2)
        answer, phrases = pd.definePhrase(input("make my day please: "))
        print('ANSWER!!')
        print(answer)
        print('PHRASES!!')
        print(phrases)
    if testNum==3:
        pd = PhraseDefiner(2)
        answer, phrases = pd.definePhrase("make my house day please")
        print('ANSWER!!')
        print(answer)
        print('PHRASES!!')
        print(phrases)

finalTest(3)


    
    
