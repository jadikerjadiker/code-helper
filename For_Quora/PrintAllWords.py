'''
allLetters = [["c", "d", "e"], ["x", "y", "z"], ["f", "e"]]
maxIndexes = [] #store the max index of each table
for sublist in allLetters:
    maxIndexes.append(len(sublist)-1)
curIndexes = [0, 0, 0] #start with the first letter choice of each letter slot
def printWord(curIndexes, allLetters):
    word = ""
    #go through curIndexes and get the corresponding letters.
    for tableNum, letterIndex in enumerate(curIndexes):
        word = word+allLetters[tableNum][letterIndex]
    print(word)

def printAllWords(): #this just changes curIndexes by one to get the next word
    while not(maxIndexes==curIndexes):
        printWord(curIndexes, allLetters)
        #go backwards through the list so that
        #we change "f" and "e" before "y" and "z"
        for indexNum, curIndex in reversed(list(enumerate(curIndexes))):
            if curIndex!=maxIndexes[indexNum]: #if it hasn't gotten to the last letter option yet
                curIndexes[indexNum]+=1 #move to the next letter todo and go on to print the next word
                break
            else:
                curIndexes[indexNum] = 0 #reset myself
            #move on to the letter slot closer to the start
    printWord(curIndexes, allLetters) #print the last word
            
printAllWords()       
'''

import itertools
allLetters = [["c", "d", "e"], ["x", "y", "z"], ["f", "e"]]
for listAnswer in itertools.product(*allLetters):
    print("".join(listAnswer))
    
    