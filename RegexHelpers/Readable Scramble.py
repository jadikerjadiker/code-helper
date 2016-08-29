import re
import random

def editText(text):
    ans = text.split()
    
    def scrambleWord(w):
        
        if len(w)<=3: #if the word is too short to be scrambled
            return w
            
        def scrambleInnerLetters(lttrs):
            return ''.join(random.sample(lttrs, len(lttrs)))
        
        firstLetter = w[:1]
        toScramble = w[1:-1]
        lastLetter = w[-1:]

        return firstLetter+scrambleInnerLetters(toScramble)+lastLetter
        
    
    for index, word in enumerate(ans):
        ans[index] = scrambleWord(word)
 
    ans = '-'*10+'SCRAMBLED'+'-'*10+'\n\n'+' '.join(ans) #join the words back together with a space in between them and put a line of dashes to separate the scrambled words
    return ans

if __name__ == "__main__":
    while True:
        sentinel = ""
        inputText = '\n'.join(iter(raw_input, sentinel))
        print(editText(inputText))
        print('\n\n')


