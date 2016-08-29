'''
2/17/16

So I've done a bit of thinking about the InputParser. Here's what I've come up with:
The main goal of the InputParser, is to take a string and turn it into some representation of known (translatable) functions that act on known phrases (nouns, generally)
There are many ways to do this, but the one that I make will be mainly based on English.
In these types of straight code, there are "words" separated by a space delimiter. In English, this is actually a space (" ").
There may be some way to not count spaces inside quotes like "hello there" so it doesn't...
try to find a function that matched '"hello' and another that matches 'there"', but I'm not optimistic about that.
The user should also be able to write a series of functions that are always run on straight code (before getting to the InputParser)...
so that the computer can more easily interpret it.
There also should be a way to insert target code into the straight code, as well as metacode...
These things should be treated as parameters if need be, but otherwise ignored.

The InputParser then works like the old one did: it goes through and pulls up all the matches for a length of words until it runs out of a match.
(If a single word cannot be defined, it asks for a definition, of course, after it is done)
It then takes the matches which spanned the longest amount of words in the actual phrase (counting the spaces left for parameters as one word) and uses those.
So it starts with the largest match in the entire string that it has found, and implements it.
It then checks to see if that messed up any of its other matches (usually be redoing the entire process right now)
It then implements the next largest, and so on, until it has a list of things it doesn't have a match for.
Idk yet how it's going to ask for definitions. The easiest way would probably just to have it print the words it doesn't understand...
and ask for you to write definitions until everything is defined.

(space delimiters, maybe quotes, someway to enter base code directly)

Also, all definitions that are made need to have the ability to ask the user questions.
There are two question types:
1. Choice
2. Free

Choice is multiple choice (an "other" option may be added later, but for now that should be hand-coded as a multiple choice option that when selected brings you a free question)
Free is free response to type a string and then that string will be returned to the program to use.
An easy-to-implement question should be yes/no (a multiple choice question)

For now, I think my implementation of multiple choice will be really lame: maybe you just have to type in the answer, or possibly it will give you a number to type as a response.
'''

'''
2/18/16
Okay, so what do I actually want this version of the InputParser to do? What do I want it to return?
I need to know the phrases and where they are (split up and everything)

So to have stuff work the easiest, I think I should have a list of all the phrases found (linked to a number)
and then another list that is just the string broken up into the phrases and they're linked to the same number.
(after typing the below example, why don't I just use ellipses to actaully symbolize space?)

For example:
"if the user has candy then make the boy happy"
could give back:
["if...then...", "the user has...", "candy", "make the boy...", "happy"]
[("if", 0), ("the user has", 1), ("candy", 2), ("then", 1), ("make the boy", 3), ("happy", 4)]

Wait, if all of these can only stop at the spaces, then the second list can be simplified to a string of numbers.
[0, 1, 2, 1, 3, 4] since we know that each time it just gets the string up to the ellipses.

Ways this could fail:
I don't see any right now. Awesome! Let's try out one of the goals.

Input:
make a function that takes a string and appends ".py" to the end of it and then returns it.

I don't think this method could actually do this at this point because it's hard to tell when the parameters are over and the actions start with just an "and".
So, I'm going to add in a "then" to make it more obvious. Also going to pretend that a prefunction took out the period at the end of the sentence.
Also assuming a prefunction replaced the "" with <""> to let the InputParser know that it's target code.

make a function that takes a string and then appends <".py"> to the end of it and then returns it
["make a function that takes...and then...", "a string", "appends...to the end of...", "and then", "returns it"]

So there are actually a lot of complicated things going on here that I can't yet deal with (not all relating to the InputParser):
Looking at the original goal, the first is that I can't tell when the parameter list stops and the actions start.
Humans can easily tell that "a string" is a noun and "appends" is a verb and separates the two.

Then there's also the issue of the word "it" and figuring out what it means based on context (get it?) (get it again?)
The only previous nouns are "a function" and "a string" so "it" must refer to one of the two.
Here it would be fine just to ask a question and clarify (preferably replacing "a" with "the")

Also, the meaning of "and then" seems pretty ambiguous too. Here it pretty much just means make a new command, which is generally done on a new line in a program.

Overall, this method has some real shortcomings that could generally be solved with tagging, but for now it seems as though it will suffice for the simple cases.

For example, the phrase:
"Make a function that takes a string and does the following: appends ".py" to the end of the string and then returns the string."
combined with the quote, period, and starting sentence capitalization prefunctions, would work perfectly fine.

On second thought, how would you deal with things like capital letters?
I would either need to be able to access to see if "Make" had any matches and if not, then lowercase it.
Or, I could evaluate it with both, and then just choose the better one.
Or it could just, you know, ask the user ;) "Is 'make' different than 'Make' (for translation purposes at the start of the input)?" Or something like that.
And that can be built into a prefunction.

Ooh, I'm getting excited because it seems like I've made a system that works like a language...
in that if you can't do something originally, you can usually find a different way of doing it which may be more convoluted, but it works.
'''

'''
2/19/16
Okay! Let's start making this thing!
"Upgrades" that need to be in this first version:
Nothing except for actually returning what is detailed above. Prefunctions should be able to take care of most of the other stuff.

Should it be called Phrase Definer?
No, because it doesn't actually define phrases.
It's more of an input parser, so that's what I'll call it. InputParser.
I'm going to replace all mentions of Phrase Definer  above with InputParser.
'''

'''
2/21/2016
The InputParser is hard to make with out a lot of examples.
So I'm going to add some of the robotics coding I did today to "goals"

The examples I'm coming up with seem far beyond the ability of this Code Helper, which makes me doubt how good this thing will be.
Plus, I'm also starting to realize how tedious answering so many questions can be, and setting it up so it works for many different cases.
There are some simple things it would be great for, but I'm not certain how often those cases come up.

So, I'm going to try to add even more examples from some of the coding I've already done on the Format1p0Loader.py
Right now the main advantage computers have over people is that they can remember things for longer and are faster at mah than we are right now.

Also, this is going to be really hard if it can't modify existing code.


'''

'''
3/16/16

I realized today that I have no plan as to what parts need to be made. No wonder I'm procrastinating!
So, I'm making a new "Planning.py" doc that will have a list of things that need to be completed.
As for now, I've abandoned doing the Input Parser because it seems like a really hard waste of time that would take forever to get working correctly
Also, I had a partially working one at some point so I figure when I want to do it better, I can. It just takes more time than I want right now.
So I'm going to move onto how the dictionnary and defining things will work out.
This will also need to work with the same output that the input parser will give out, so I'll try to be careful to keep that in mind.
'''