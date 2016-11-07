'''
Goal: take input and use the phrase recognizer and dictionaries and other resources to generate the translation



Test Cases:

print ||make all upper case||hello everyone||
Should return:
print("HELLO EVERYONE")
Should do:
Check for lowest parentheses level (make all upper case and its parameters)
Evaluate the stuff at the lowest level (within each other lower level) so it evaluates ||make all upper case||hello everyone|| and gets back "HELLO EVERYONE"
Then evaluates the higher level (print "HELLO EVERYONE") to print("HELLO EVERYONE") and returns that.


|^|^print("hello")^|^|
Should return:
print("hello")

||tab||print("hello")
'''

'''
So right now we know that we want it to evaluate the lowest level stuff inside each level
(if you were to draw a tree map of the levels, we want to hit all the lowest braches on each swoop)
And it's looking like it might be easiest if the symbols used to be recognized are changeable so that I can test out which forms are easiest to use.
Should I deal with that now?
At first I think no, nothing extra. But on second thought...
It's something that will be hard to add in later (unless I shuffle it off into a separate function...)

Assuming I shuffle it:
So I want something that will divide the code into parts (each part is a string) and that string is associated a "level", and a codetype.
If "print 'hello'" is typed in, it would all go as level 0 (the top level, last stuff that should be evaluated) and its codetype would be 2 (straight code)
On the other hand, if "print '|^|^2+5^|^|' " is typed in, then the "2+5" would be level 1 with codetype 0 (basecode)
And print ||numtostring|||^|^122+1^|^||| would be organized into
122+1 level 2 codetype 0, umm... how do I notate that something's supposed to be inside of the base code parentheses...

So the organizer needs to have the code part to be evaluated (as a string) where some of the string can reference other parts of the table.

_-_ looks like a good preface to a number in the table... Let's use it for ILs first (done in another comment below)

The question is how to notate the insertion of a certain value within the string... string.format uses {} as an identifier...
I think I should just use the general identifier with a new symbol and be done with it. The symbol is "gett" like "GET from Table".
So if string #2, needs the evaluation of string 1 it will put _-_gett_1_-_ in that spot.
Luckily I shouldn't be doing this by hand often... 'cause that looks like a fingerful.

Why is a level needed if we just put everything that's low level first? It's not. So there doesn't need to be one.

Okay so redoing these test cases:
"print 'hello'":         (Should give the result of...)
["_-_2_print 'hello'_-_"]

"print '_-_0_ 2+5 _-_'":
["_-_0_ 2+5 _-_", "_-_2_ print '_-_gett_0_-_' _-_"] (I decided that each entry in the table needs to start with the IL)

"print _-_1_ numtostring(
'''

'''
So, how do I want this metacode stuff to work? Let's come up with a few examples.

I want to be able to "tab" stuff. I also want to be able to convert to a condition.

So let's have each parameter be separated by a comma and if that part needs to be evaluated we can use an indicator _-_eval_ stuff _-_ on that one parameter.

What if the metacode definitions had access to an evaluator? Is this even possible (easily)?

So let's say we want to write that tab definition again... actually...
When you pass stuff into the metacode, is when you should figure out what's going to be evaluated or not. The metacode shouldn't have to deal with any of this at all!

So if you're doing _-_1_tab(something that should be evaluated as straight code here)_-_ then it should look like
_-_1_tab(_-_2_ something _-_)_-_ and the organizer will look inside the parameters of a tab to see if anything needs to be evaluated beforehand.

So what if we want to do something where something that the metacode creates needs to be evaluated? Will this ever be needed?
Let's say it is needed, but if it's too hard to figure out then I'll assume it's not for now.

This really depends on the structure of the organizer, and what is available to what. Should we be able to evaluate stuff at certain input levels INSIDE the definitions.
Let's say I want to have a printThenTab metafunction that literally first prints the string that's given to it, and then puts a tab at the start.

I want to be able to use metacode inside my definitions so I can just say (I'll put in the IL even though it might be assumed later on)
printThenTab(^$1$^):::_-_1_ tab(_-_1_ printWords(1) _-_) _-_
as the definition.

Basically, the metafunction is written in metacode instead of basecode, so we need something to run metacode.

I think it should be called the evaluator. It can run both straight code and metacode.
Wait... should straight code be allowed in metacode?
1. That could create a loop, where they use eachother in their definitions...
2. Straight code changes between projects and should be changed by the user.
3. Metacode should not rely on straight code to function because straight code definitions should me modifiable!
STRAIGHT CODE IS NOT ALLOWED IN METACODE DEFINITIONS! ONLY METACODE AND BASE CODE ARE ALLOWED!
Likewise, metacode is obviously not allowed in base code. They are 3 separate languages, where each one above can use the ones below.
The cool part is that the top two level languages are created by the user.

This also means that straight code is never run. It is only translated.

I have two different meanings for base code that need to be separated. 
1. The first is the bottom code that the straight code is translated into.
2. The language (Python) that actually does the translation. The language that the metacode definitions must be written in, and the language the entire translator is in.

(1) is going to be called target code from now on, since its the code were trying to get the straight code into: it's the "target".
(2) is going to be called base code like before. It's the base language that controls everything else.
'''

'''
So now, we've got an evaluator... What is its job?
The evaluator should take a string with an intitial IL and run the metacode and basecode that the string has in it.
So for example if given "_-_1_ tab("print('hello world')\nprint('done')) _-_"
How does the evaluator know what to evaluate or not? Based on whether or not stuff is in a string or ouside of it?
Yes. Everything outside of a string needs to be converted.

So the evaluator is like a program runner for metacode. You give it stuff, and it runs it. It can run both metacode and basecode.
'''

'''
So let's say we don't want to use metacode: the definition for our straight code is written in base code.
Is this base code allowed to modify stuff? Absolutely! Is this accomplishable?

set ^$1$^ to ^$2$^:::1 = 2
Is there a way to store this without functions? How would a reader read this?
Let's say it is a function, cause that seems easier.
setTo(item1, item2):
    return "item1"+" = "+"item2"

So it seems like it wouldn't bee too hard to have the computer write functions like this and use them. Let's leave it for my future self to figure out. I'll enjoy it.
'''

'''
I'm thinking for metacode it would be best to do everything like a function. So just "numtostring||params||", (pretend the || are parentheses), nothing at the start.


There should be only three entering "spaces" and definitions should be assumed to be entered into one of those three spaces.
The spaces are:
IL 0: base code _-_0_ (this is pure Python (or whatever language this Code Helper is ported to))
IL 1: metacode _-_1_ (these are the functions that are used to provide a secondary layer between base code and straight code, so code is reusable between phrase definitions)
IL 2: straight code _-_2_ (this is the code the user will type in to be converted to the target code.)

So right now these IL (enter level) identifiers are in the form _-_symbol_ write whatever you want here _-_ now outside of that enter level.

Parameters of metacode functions are assumed to be in base code.

The definitions of the phrases/functions in straight code/metacode are assumed to be in the code below them (metacode/base code respectively).

Within each space, having nothing assumes it's still in that form.
When displaying the definition for each wordtype it should display the appropriate symbols beforehand so you know what IL you're in.

okay, so a string containing metacode to run would look like:
_-_1_ add("a", "b") _-_
and when run by the evaluator would produce "a + b"

So how would it work if I wanted two versions of the setEqualTo metacode...
one that had spaces in between the vars and one that didn't, where the end always had a boolean?
ALL PARAMETERS OF METACODE FUNCTIONS MUST BE STRINGS unless they're in a different IL
so _-_1_ setEqualTo("a", "b", "True") _-_

would then have the definition:
setEqualTo(0, 1, 2):::_-_0_ if 2==True:\n\treturn "0 = 1"

'''

'''
12/8/2015
First of all, the Input Level symbols have changed to be similar to HTML hashtags for usability.
Straight Code: <il2>stuff</>
Meta Code: <il1>stuff</>
Base Code: <il0>stuff</>

I'm worried about having numbers in the parentheses. What if the function is something like:
addOne(1):::<il0>1=1+1</>

Then how would the evaluator know what to do? It wouldn't.

So what we did use numbers (it seems right and easy for the computer to do so) but they were surrounded by hashtags?
addOne(#1#):::<il0>return #1#+1</>

So then what would happen if someone wanted a function that would take a string "a" and make it look like "#1#a"?

The way this is normally dealt with is that special characters are prefixed by "\" by the person who types.
But I want to make things easier on my user... So what if special characters were found and that was added to them in storage?
Does that allow for ambiguity? It sure seems to add in a lot of "/" symbols...

How about I use "$"? It's a sign that's not used a ton elsewhere...

So then that function that would take a number "a" and make it look like "#1#a" becomes: 
appendHashOneHash(#1#):::<il0>return "$#1#"+#1#</>

So that when the evaluator sees that definition run on the string "test" it will run:
return "#1#"+"test"

But somthing seems wrong here, like there's room for misunderstandings still...
I noticed that whenever this escape character system is used, the escape character only escapes the next character in the string. Not a series of them.
It also generally takes away special meaning, which is the same as what I was doing above.

So how about instead of using two hashtags, I only use 1? I know it clashes with Python's comment system... But Python also decided to use it because it was so easy.

But then how do I know when the number is over? I don't think there will ever be a situation where things are next to another number...
like #1 is next to 123 so it looks like #1123. #1 or any other parameter must be operated on. putting a number next to something never operates on it. So we're good.

Here's the overall main idea then:
You type in something like "if Mary is happy then make Johnny happy" and want it converted into Java
And the computer recognizes nothing, so you have to define the phrases: "if ^$$^ then ^$$^", "^$$^ is happy", and "make ^$$^ happy" like so:
if condition then runThis:::<il0>return "if ("+condition+") {\n"+<il1>indent(runThis)</>+"\n}"</>

Is there any time where there will be logic inside of a base code section? Yes. Something like "the bigger of the two: 1 or 2" could use some logic.
Also could do "print hello version 1" etc.

The computer will store the above definition as either:
if #1 then #2:::<il0>return "if ("+#1+") {\n"+<il1>indent(#2)</>+"\n}"</>
or
if ^$1$^ then ^$2$^:::<il0>return "if ("+1+") {\n"+<il1>indent(2)</>+"\n}"</>

the first one seems more likely though... I'd just need something that put a backslash before every string of numbers and...
every backslash before it saved. But then how is "\\123" interpreted? Was it "\variable" which just happened to be the 123rd variable?
or was it "\123"... nope it can't be. This should work... 
It does bother me though that this hinges on not having numbers next to parameters.

Todo let me look at how my phrase definer expects definitions to be written.
It expects something like "if ^$$^ then ^$$^" to recognize the phrase.
The evaluator has yet to be written, so I don't know what that needs.

indent is a new metacode function it doesn't recognize, so you must define:
indent(#1):::<il0>return #1.replace('\n', '\t\n')</>

Note that everything up to and including "<il0>" and then the "</>" at the end is provided by the computer...
(with an option to change the input level) so you really aren't typing all that much.

What bothers me is that above thing with all the pluses and whatnot and how long it takes to type and how unnatural it is.
Oh well. I'm just going to have to deal with it for now. It's not that hard.

So the person typing the definitions only has to make sure that whatever they type to fill in the ^$$^s isn't later in the definitions.
Second definition:
someone is happy:::<il0>return <il1>getCharacter(someone)</>.happy==True</>

getCharacter(#1):::<


Todo: possible issue: what if the actual phrase has ^$$^ in it?

'''



'''
NO LONGER IN USE!!!:

The copied-over symbols list:
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
'''