'''
12/11/2015

I need to do some new thinking about this project. It's taking a lot longer than I had hoped to get it to work.
I like the idea of what is currently called the PhraseDefiner. It allows words and symbols to encompass other words and symbols and manipulate them.
I think that should be kept in between the two versions.

I also like the file storage technique and I love that it's human-readable and very modifiable.

The two things I would like this project to do are:
1. Work most of the time. If it has some bugs, that's okay. It's the idea that counts.
2. Be easily changeable. This is why (1) is okay; because if it's broken, it's not too hard to find out where things went wrong and replace it.

So let's rethink this idea.
I want someone to type in some symbols.
The computer finds the symbols it knows. (Here, "knows" means "has a rule to translate it into the other language")
If the computer knows all of them:
    it continues.
Else:
    It uses a method to learn them. (Currently this method is asking the human to define them in code. Maybe someday it will be able to look online on its own.)
It follows the rules.
It gives the user an answer.
'''

'''
12/11/2015

So, what's the easiest possible way to go about doing this? I'm going to copy the general flowmap:
1. The computer gets some symbols.
2. The computer finds the symbols it knows. (Here, "knows" means "has a rule to translate it into the other language")
3. If the computer does not know all of the symbols, it uses a method to learn them. (Currently this method is asking the human to define them in code. Maybe someday it will be able to look online on its own.)
4. It follows the rules.
5. It gives out an answer.

Easiest way to do this:
1. input() function.
2. Different version of the phrase definer, now that I've got some more standard symbols
3. Print out all the symbols you do not know, and ask the user to define stuff until everything is defined.
4. Make something that will convert the understanding of the phrase definer into an actual program with an output.
5. print()

So, I'm going to change my goals.
The first thing I want to get to work is the file reader and storer, and I want them working almost perfectly and smoothly and quickly.
The next thing I want to do is a revised version of the phrase definer that works for any language that has these types of symbols. (I want it to be less dependant on space in-between words)
'''

'''
11/20/2015
Here's a more detailed overview of the actual conversion process from what I know right now.

The PhraseDefiner will take in the straight code and split it into known phrases and use another class to get the unknown phrases defined.
Then, the Evaluator will take the phrases from the PhraseDefiner and convert it to target code (it will use a recursive method)
Then, I'll make another class to print out the output.

Not too much work. Lots of thinking, but not a ton of work.
'''

'''
1/6/2016
I put some of my newer thoughts on the PhraseDefinerThinking file (may later be changed to the PhraseFinderThinking file)
'''