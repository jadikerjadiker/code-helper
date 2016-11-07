'''
This class needs to be able to:
*Quickly return all of the phrases in the dictionary that start with a certain word as a list of phrases
*Quickly return the definition of a phrase

Thinking:
Okay, so I need to figure out what the dictionary, high code, and all this other stuff is going to look like at the base levels
I still hope that this gets rewritten to be better in the future, so this doesn't have to be amazing, it just has to work (at a moderate level)
Do I want it to deal with newlines inputted into the porgram?
No, that seems unneccessarily complicated, especially given that I've already written the definer (that doesn't deal with them)
Do i want the translator to deal with newlines? let's see...

What sorts of things would I like to be able to do with this bad version of the program?

my easiest example: "set <<a>> to <<3>>" should print back "a = 3"
My example of something that probably won't work on this one, but should be able to work after some upgrades:
"if James is happy then show a lollipop at the middle of the screen" ==> "if James.happy:\n\tlollipop.show = True\n\tlollipop.x, lollipop.y = getScreenCenter()"
The main upgrade that is necessary for Python is the understanding of tab levels, and that new lines of codes...well... go on new lines XD

The code for the above things I imagine would look something like (<|| high code ||> I like this symbol for high code):
set ^$1$^ to ^$2$^ ===> ^$1$^ = ^$2$^

where ===> signifies a definition, and ^$something$^ just declares a variable "something" that will be used later with whatever code is in that slot subbed in.

Where high code comes in though is for the second one:
The main interesting definition:
if ^$condition$^ then ^$action$^ ===> if <||formatCondition(^$condition$^)||>:<||tab increase||>\n^$action$^
The definition of the parts:
#needs re... not sure how to deal with that quite yet
def formatCondition(con):
    return re.sub("=(?!=)", "==", con)

High code currently just means something that you want to compute behind the scenes and not spit out...
But there's a difference between that and writing out the definitions of all the high code in python.
I think the python-written definitions should be called base code.
So you have normal code "" (code to be translated), straight code <<>> (to be used as-is>>, high code <||||>(to be run behind the scenes), and base code (defined in python)

Should you be able to access high code by writing normal code??
Right now, my answer is "only in definitions".
Rationale: If high code were accessible in normal code, it would seem odd, as it's a part of your program that would be run behind the scenes... it just seems odd.
I feel like it would be better to have to write a normal code word whose definition was to run the high code on something.
It separates the behind-the-scenes stuff from the casual user.
The reason for high code in definitions is that definitions are exactly where we want things to happen "behind the scenes", where the user types in something,
...and the computer uses the rules/high code to output something completely different.

So what's the diff between high code and base code?

high code can be originally defined in normal code, and should be turned into base code after that original normal code definition.
Should it retain its normal definition in case the base code would change based on new definitions? Yes, but not at first... just need base code definition for now.
I don't want the translation of the words to be changing as I test this thing out.
In the future it would be the best if when a word has its definition changed, if it's a strict upgrade, you can choose to upgrade aeverything (now or at a later time)
...(sort of like Alpha Centauri, except it takes time instead of credits), and if the definition changes some stuff, go through and choose which ones to upgrade,
...or if you wnat to, even write a function that can go through and decide for you, and ask if it's not sure
It might even be best to save them as different definitions with numbers so that the old programs reference the same word, or code, just a different number.
...and the number can be brought out into a new word if need be too.
I'm tired now, which is perfect for dreaming and imagining.

base code is defined explicitly in Python (it's actually Python), and performs the inner/base layer of the program. This base is used to do things it's never done before.
(such as learning what a tab level is, where \n is replaced with \n\t for each current level)
but base code can also be used to do things that it has done before, and can be used as a "caching" or permanent saving mechanism for definitions.

The dictionary, dictionary reader, and translator need to understand all this ans how to use it... This is going to be fun :D

So it seems like normal code is code that is pure substitution, high code involves something other than substitution, base code is how the computer understands all this stuff. 

'''


class DictionaryReader:
    def __init__(self):
        pass

    
        
