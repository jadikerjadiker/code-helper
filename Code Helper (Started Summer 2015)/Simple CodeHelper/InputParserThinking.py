'''
2/19/2016
In my thinking on the thinking page and elsewhere, I've been using ellipses (...) to signify the parameter slots in a phrase,...
which totally makes sense to me.

But I also want this to be changeable. So I think that the programmer should be able to specify what symbol is used on the format page.
And I can just load that into the system and treat it as such. Cool. What should it be called?

Uh-oh. So this is why I made the format pages in the first place, right? So the settings would be easy to access.
So is this actually easier access? I would argue yes. But it's not clear from the page what attributes it needs to have, which sucks.
In other words, if the "changeability" permeates all the way down to the actual format page, things can become complicated.
But then that's the user's choice. The defaults are what should make things easy to use, and making things complicated should be easy ;)

So the name should be "Parameter Slot Symbol" where capitalization does matter...
(todo upgrade: it shouldn't matter, but this is just easier to program for now)
 
Next, how should target code (or other things that should be counted as parameters, but aren't a phrase) be labeled?

There are two possible methods:
1. Just have a symbol that replaces it in the string.
2. Have an open and close symbol that wraps the target code (like parenthese wrap this) of which the inside is counted as a...
must-have phrase that will be put into the lists as an actual phrase...
You know what, 1. is easier, so I'm just going to do that. A prefunction should deal with whatevers going to happen there.
The name for this symbol is "Do Not Parse Symbol".
'''

'''
2/20/2016
Previously the way this worked wasn't all the greatest.
Basically, theres a list of all the possible phrases that could be included in the phrase, and it's slowly cut down as phrases fail to match.

But, that might be the easiest method to program, which is the point of this version: to just get things done.

The main issue it ran into is if you use a phrase that it's expecting after a parameter slot inside a parameter slot, then it doesn't split versions.
I would really like to have the functionality to deal with that, but it's not completely necessary.

Plus, I'm not exactly sure how to implement the "longest wins" rule.
First, it must be done in terms of words, not characters.
Second of all, I think that generally things with 3 or more words together should probably go together.
But maybe I'm wrong. And the old version worked alright (in fact, I'd probably use it here if I hadn't run into some strange bugs I didn't want to have to fix).
Should the "longest wins" rule include all the words inside the parameters? This makes short phrases with one parameter slot ideal.
Which is not what I want to be ideal. So no. It's based on the word length of the actual phrase.
Does the parameter slot count as a word?

Quick thinking about evaluator:
it needs to go through and add to the end of the number list the phrases that have slots at the end.
'''

'''
3/16/16
Okay, so this is going to take way too long to program.
So I'm going to skip this and create the next part which hopefully will be easier, and create some way for the human to easily type in stuff.
'''