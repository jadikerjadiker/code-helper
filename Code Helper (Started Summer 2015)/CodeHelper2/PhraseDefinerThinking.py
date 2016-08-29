'''
12/15/15
PhraseFinder Thinking

The goal of the phrase definer is to take a bunch of symbols, figure out which ones are not understood, and which symols operate on which other symbols.

The goal of this PhraseFinder is to take a string and convert it into a tuple of two arrays.
The second array is a list of all the portions of the string that it understands. If a certain phrase is split up within the string, that phrase will also be split up here.
For example, string:"make Jane happy" would probably result in ["make", "happy"] if the computer didn't know what Jane was.
The first array is a list of tuples with two lists inside of them. Each tuple is comprised of (first value) a list of all the complete known phrases,...
and then (second value) a list of all the indexes that refer to the second array that the phrases came from.
For example, the first array for "make Jane happy" would be [("make happy", [0, 1])]

To give a more complicated example:
string:"if Joe is sad, make the sky dark". The computer knows how to deal with if statements (and the comma that tells it to end the if statement),...
how to check if something is sad, and how to make something dark but it doesn't know what Joe and the sky are yet. It should return:
([("if , ", [0, 2]), ("is sad", [1]), ("make dark", [34])], ["if", "is sad", ",", "make", "dark"])

Is this the best way of doing it? I feel like it's kinda clunky, and I'd really like some symbol to stand in for words or somthing...
Maybe I should just have it give indexes of characters as to where certain phrases start and end. Then it's less human understandable, but this part doesn't have to be.

Here's one thing I would like to impose: when a phrase acts on "SOMETHING", like "I threw THE BALL",...
if you want there to be two objects there, you can, your function just needs to specify it. It is not the job of the PhraseFinder to try to figure out...
where the difference between two objects withing one phrase "slot" should be put, if that makes any sense.
'''

'''
11/19/2015

I pretty much agree with my earlier thinking.
The PhraseFinder should only be there to specify which phrases are used and what should be plugged into the slots of those phrases.
Let's call this the Slot Method then. All phrases can have slots where other strings can be input;
Is is the job of the function to deal with/understand what's in the slots.
Unless told otherwise, the Code Helper will convert everything inside the slots beforehand,...
so "the player is winning" may show up in the function as "True" which is how it should be.

So what's the easiest way to represent this?
The goal is to pass it to something that will start converting the code into targetcode and can plug it into the phrases and know the order easily.
Before it was easier because I was just dealing with words (separated by spaces). But now I can just deal with characters.

Will the method above work the best? No; no character numbers. But wait, the character numbers shouldn't matter.
It should just be the phrases, the order, and what goes inside what.
So yes, the one above should work. And if it doesn't, I can just redo it how I want it to work.

Next, how should this thing ask for definitions? Does it go to a completely different class? Yes, in order to separate the two.

What information does it need to give to the class in order for the class to be able to ask human questions?

So here's a weird English rule: everything has a space after it except for the words at the end of a sentence.
So how does the phrase definer understand english if stuff with a period after it is different than stuff with a space?
Also, the word "and" is bothering me a lot because if you say "make John and Jake happy" then "make ^$something$^ happy" with "John and Jake" should then convert to...
"make John happy and then make Jake happy". So should their metafunction inside the "make ^$something$^ happy" have to deal with that every time?
Because it's a repeated pattern. If I want to say "make ^$something$^ sad" and use "and" it follows the exact same pattern.
But right now there's no easy way to tell the computer that it follows the exact same form. The metafunction has to be written inside of the original phrase (I think).

Let me think a bit more about this issue.

I think having that metafunction may actually be the fastest way of doing it. To write a function called "convert and" that's used on the input and then loops through.

So the definition for (nts: I have no idea if this is anything like how definitions will actually be done) "make $^something^$ happy" will look like:
<il0>#Python shouldn't care about a newline here, which is nice
ans = ""
for person in <il1>getAndObjectList(something.strip())</>:
    ans+=(person+'.emotion = "happy"\n')
ans+=ans[:-1]#cut off the last newline
return ans
</>

So if you put in "make Jim and John happy", the metacode getAndObjectList() will take "Jim and John" and return ["Jim", "John"] so ans will be...
'Jim.emotion = "happy"
John.emotion = "happy"'
Exactly like it should be. Now what annoys me though is that I have to strip out that space. Which is pretty much the same annoyance...
So let's keep it like this for now.
'''

'''
11/20/2015
So the Evaluator needs to know what the stuff at the lowest level is. Is that easy to find in our current method?
Let's assume it does actually know what everything means so we plug in "if Joe is sad, make the sky dark"...
and the PhraseFinder gives back (assuming it ignores spaces and I'm not typing that it recognizes what it should just ignore):
([("if,", [0, 3]), ("Joe", [1]), ("is sad", [2]), ("make dark", [4, 6]), ("the sky", [5])], ["if", "Joe", "is sad", ",", "make", "the sky", "dark"])

Yeah, it seems okay to understand. Just look for phrases that have gaps and look for what they need to be filled in with in what order. It's doable.
My main issue is that the way I'm thinking about making the real one, there will be so many empty spaces in both lists that I'm not showing here.
It may take up a lot of memory. I'm just going to go with this for now and hope the space issue can be solved later.


Just went through and replaced all "PhraseDefiner" with "PhraseFinder" because that's what I'm changing the name of this class to. It just makes more sense.
I assume the PhraseFinder will be the class that asks the human to define phrases.

Actually, the above thing does not work because for example the Evaluator doesn't know if "Joe" is plugged into "is sad" or if "is sad" is plugged into "Joe".
What was my old method? Just looked at it. Doesn't deal with characters and has a lame way of telling what is inside what.
'''

'''
11/21/15
so the main issue now is: how do I know if I have two phrases in the form "phraseOne ^$$^" and "^$$^ phraseTwo" which one should be plugged into which?
Hopefully only one would support nothing as an input, but I don't want to have to look at definitions in order to understand that.
I can go back to the model of asking the human.

I think that that would be the best choice here. If the computer is unsure, ask the human.
So maybe that's actually what I need to make next: the part that will ask the questions.

Because how the PhraseFinder is made will depend on the question asker.
'''

'''
1/6/2016
But how the question asker is made will also depend on the PhraseFinder, so I should just start and then see what happens.

If I don't like it, I can always redo it.

So, let's get some specifics.

PhraseFinder is given a string. Its job is to use a dictionary reader module/class to find phrases within the string that make the most sense.
Then, it needs to have some sort of response that links the phrases scattered among the string to the phrases it knows...
and then if there are words still left to be defined, passes this response to a PhraseDefiner (maybe along with some better recognition of what needs to be defined)...
that will then use a question asker to ask the user and get definitions for phrases. It will then repass the string...
(probably every time it gets a new definition, just to see what still needs to be defined).

So this thing needs to be very efficient.

My last version of this generally defined "most sense" as the largest (in terms of characters) took precedence over the smaller phrases...
This seems to be the best way to go for now since it makes sure that phrases are being interpreted over words.
My issue with it is when long strings are passed, then long phrases may be distributed around that may not mean what the user meant. But this should work for now.

It's seeming like a later must-have upgrade is to be able to tell the PhraseFinder what is a phrase and what is not.

Wait. What if I just did that and then wrote a PhraseFinder later?

How would a human version of this work?

I think I'm going to just make a really really really simple version of this and see what actually should be done by the computer.
'''

