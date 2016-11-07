'''
Order of attack:
1. 
'''

'''
test cases:
_-_1_ add("a", "b") _-_
gives: "a + b"

_-_1_ setEqualTo("a", _-_1_ add("b", "5") _-_) _-_
gives: "a = b + 5"

_-_0_ _-_1_ tab("one line") _-_ + _-_1_ tab("\nline two\nline three") _-_ _-_
gives: "\tone line\n\tlinetwo\n\tline three"

_-_0_ _-_1_ tab(_-_0_ "one line" + "\nline two\nline three" _-_) _-_ _-_
gives: "\tone line\n\tlinetwo\n\tline three"

_-_1_ tab(_-_0_ "one line" + "\nline two\nline three" _-_) _-_
gives: "\tone line\n\tlinetwo\n\tline three"

_-_1_ tab(_-_1_ add("one line", "\nline two\nline three") _-_) _-_
gives: "\tone line\n\tlinetwo\n\tline three"
'''

'''
Okay, so this evaluator needs to be able to run metacode and base code (python)

This is the only thing that will run metacode or basecode, so everything that runs stuff has to be a part of this.

You should pass it one string, and it will run the code in that string and return a string.

So what is the format of this string that is given to it? Is it just one statement of metacode?

Let's start with the simple version: the conditional.

let's call the function "cond" and it just converts equals signs into double equals signs. 
To make it stupidly easy, it literally converts every equals sign into two.

So when it looks up the function "cond" it will get this definition:
cond^$1$^:::1.replace("=", "==")

So what the interpreter will need to do is create a variable called 1. The easiest way to do this is to use a table.
t = {}
t[1] = "some value from the string"
CORRECTION:
The easiest way to do this is to have a dictionary where the key is the value inside the ^$$^ and...
the value is a number from 0 up that corresponds to it so that the table is a list of all the "variables"

And then it will have to run the code 
"some value from the string".replace("=", "==")

and get the value. This will have to be done using exec (or eval)

So how customizeable do I want this to be?

The parameters can have any names they need to have in the definition so that they're unique within the definition.

I don't think more than one function of metacode can be done in one string though right?

All a metafunction does is it takes strings and spits out a string. Having two metafunctions Next to eachother does nothing.

If you want to combine two strings, then it should be a metafunction join(string1, string2):::_-_0_ return string1+string2 _-_
'''

'''
Let's say I get the definition
add(a, b):::_-_0_ a+b _-_

And the phrase is "_-_1_ add("word", "word2") _-_"

So overall I know I have
[add(a, b):::_-_0_ a+b _-_, "word", "word2"]

So first I need to create a dictionary (they're created like a = {key:value, anotherKey:anotherValue})
'''