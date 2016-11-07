'''
Overall structure of the program:
Graphical (or non-graphical) User Interface is run by a CodeHelperGUI
Translator takes what is entered.
Translator then uses the phrase definer to determine what parts of the input it understands. #nts: this would be where parentheses could notate complete phrases
Something (I don't know the name yet) then asks questions and prompts the user for responses to get definitions.
Then another part of the translator converts the straight code into metacode and basecode (whichever is easiest)
Sends the metacode and base code to the evaluator which spits out the result
takes the result and displays it (in a copiable form) to the user

So basically:
display method to enter problem
get problem
understand problem
solve problem
display results
'''

#nts: (11/23/2015) It may be useful to start putting all of these different classes I'm using into more compact files so I don't end up with like 100 files...
#and smaller portions of the program are easier to find and edit.

'''
Things it will do:
Translate based on definitions
Metacode
Variable names in definition parameters can be whatever the user wants.

Limitations for simplicity:
Keep track of level of phrase (how does this work with both metacode and straight code?)
No caching yet
No parenthetical "i want this evaluated first" stuff yet
Only one definition per phrase (annoying, I know, but this just needs to get done. I can redo it later if I want.)
No context (I'm not exactly sure how to use/implement it yet, so I don't want to be slowed down by it)
No phrases that can take an unknown amount of parameters (Nothing like "Create an instance of a bike, a cow, a horse, a ...)
Not a lot of customizability of the metacode and definitions and such. This can be added in later, but I'm not sure what I want the thing that
the current symbols to look like right now so I'm just gonna skip it.
'''

'''
So the goal here is to take what they input in some language, whether it be english or something else they have taught the computer.

The computer will then use what it "knows" to translate what they type in into another language by using functions the person has set up to do so.

Steps:
1. Get input from user
2. Interpret input
3. Display output

1: Right now I'm using tkinter but that won't work on here so I'll probably just end up typing it straight into the code (or maybe learning how to do HTML forms)
2: 
Let the user define phrases that it thinks the computer won't know. If the computer does know that phrase then bring up a warning about overwriting a current phrase.
Check for known phrases and match them against a dictionary, starting with the longest known phrases (no ranking mechanism yet)
Send these phrases to a translator which uses the dictionary(ies) to translate them into the correct language (I NEED A SYNTAX AND WORD DICTIONARY TO MAKE IT SIMPLER) (each dictionary only holds one language)
3: display what the translator returns

So what are definitions? Definitions are functions that can be apllied to a phrase that turn it into a phrase of lower (or possibly equal) level.
The goal is to get it down to all level 1 phrases which can then be directly translated to whatever base language was taught. 

Test Cases:

"set a to 3"
should become
a = 3

"if the person is smiling then print 'the person is smiling'"
should translate to
if person.smiling == True:
    print('the person is smiling')

"loop 10 times"
should become
for i in range(1, 10):

How:
Since the "if" statement one seems to be the most complicated, let's start there.
"if ^$1$^ then ^$2$^" means
1. Translate the ^$1$^ with the context of "if" (What's the point of context? Is it needed? How does it work?)
2. Step 1. should give "person.smiling == true" (pure Python, so we go all the way to level 0)
3. Take what is recieved from the translation (^$1$^t) and turn it into "if ^$1$^t:"
4. Translate ^$2$^. For every new line in ^$2$^t add a tab right before it.
(So this is where I start wondering about metacode. Should there be a seperate metacode defined to "tab" in an area?
I don't want to have to type it out again...
Should it have it's own metacode language that's in the same organization process as the normal stuff?
What are the problems with this?
Let's say I define ||tab|| ^$1$^ as ||replace all '/n' with '/t/n' in|| 1
Then ||replace all ^$1$^ with ^$2$^ in|| ^$3$^ is defined as 3.replace(1, 2)

The issue with all these definitions using phrases with other definitions is that it takes more time because it keeps on having to translate down before running pure Python.
So either I need to get some sort of caching thing going, or the "compiler" has to translate all these things every time.
I think the easiest kind to make would be a fast dictionary where any definition that was used was then loaded into the fast dictionary as pure Python

The perk of them is that if there's a better way of doing something, then all I have to do is update that one thing and the rest of the functions that use it will be updated.
Another issue is adding definitions to phrases, since there'd have to be a way to either figure out what definition to use (based on context (which I don't know how to do yet))
or it could ask the user which definition to use (every time?!) or the program could be dated and it uses the definitions of that date (something like that)

The reason for metacode is that there may be some terms that have different meaning when used to translate code versus when turning code into a different language.
Having metacode require a signal allows the same words to be used and hides the definition more from the casual user.

So, is there going to be metacode? Pros and cons:
Pros:
Allows definitions to be written much faster and easier.
Allows basic users to not have to program much even if they have to write their own definitions.

Cons:
More work for me
It's like a language within a language; a bit confusing
Could make it less straight-forward to find out what a function actually does.

Pros win out. Metacode will be added this first time around (unless it turns out to be more complicated than I bargained for.).

'''

'''
So, metacode. How is it going to be used and signaled?

I think all metacode should be written like a function in the form
||funcName||param1, param2, param3, ...||

You know what? Let's start with normal definitions and then move on to metacode definitions and then come back to how they're going to be used.

I select the phrase "set...to..." to define (somehow).
The definition should be written as:
set ^$1$^ to ^$2$^:::1 = 2
The "^$1$^" represents whatever went in the first gap and the ^$2$^ represents what went in the second gap.
The ":::" signifies that you are about to start the definition (and you have finished with defining how many parameters there are going to be, etc.)
Then, after the triiple colon, whatever symbols are inside the "^$" and "$^" stand for whatever was there when it comes time to evaluate. They're essentially parameter names.
It is assumed that everything on the other side is the Level 0 (the base language you want it to translate to) if not...
Then it's metacode (I don't think I'm going to allow straight code into definitions)
'''

'''
Okay, so I'm having issues coming up with symbols that are easy to use and haven't been used before.

The issue is that I'm going to have a bunch of places where people are typing in different contexts.

Contexts:
Typing straight into the translator (hoping for your code to be translated correctly)
Defining straight code
Defining metacode
(Hand-typing into the dictionary) (This may be counted as another context but I'm not going to focus on it because nobody should have to do that.)

So a big part of the translation is figuring out what type of code stuff is and in what order to evaluate it in.

It seems like I'm leaning towards having translators between each different part of the program... Which seems pretty unnecessary, but may be useful.
'''

'''
I'm sick of trying to do this "right". I'm just going to get it done.
Metacode is necessary if this thing is going to be even remotely useful.
'''

'''
Okay, so this IL (input level) stuff like _-_ILnum_ codeStuff _-_

Does that signify something to always be evaluated?

Is there anything in here that isn't evaluated that isn't in a string?
No. In fact, usually the stuff that is evaluated is inside some sort of string.
Thus, yes, the ILs always imply that what's inside of them is to be evaluated (at that level)

The quotes themselves are basically IL indicators of target code (IL -1 if you will).
'''















'''
OLD STUFF GOES BELOW THIS! THE THINGS BELOW THIS ARE PROBABLY INCORRECT!
'''



'''
Symbols:
Entering code into translator (enter level 0 (EL 0)):
Straight code: Nothing needed
Metacode: ||funcName||params||
Base Code: |^|^basecode^|^|

Entering code into straight code definition (EL 1):
Straight code: --||straight code||--
Metacode: ||funcName||params||
Base Code: Nothing Needed

Entering code into metacode definition (EL 2):
Straight code: --||straight code||--
Metacode: ||funcName||params||
Base Code: Nothing Needed

Note: metacode "params" is EL 0

"Nothing needed" means that if no symbol is used it will assume the phrases are of that type.

Dictionary code is completely separate.
'''

'''
I'm going to need to learn how to make those HTML forms for communication...
'Cause all this asking for definitions and stuff, I really don't want to have to program in by hand beforehand.
That'd be slow and useless.

But for now, the GUI is kept separate from the programming so it should be able to be changed at any time.
'''