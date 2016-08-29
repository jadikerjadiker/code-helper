'''
So when and how do I use memory?

Right now, it seems like an easy way to code in those variables like "the boy" is 'boy' and stuff like that.

So what's the difference between _mem and __metamem?

__metamem is stuff that's inherent to the UI itself. Nobody should mess with it, but programmers may want to.

_mem is used for everything else.

So let's say I want to have this basic "askQuestionAndGetLongResponse" function that can be used in all these other functions I write.
What type of memory does it belong to?

Umm... It doesn't belong in memory. It belongs in the user-defined functions file.

So everything that comes originally 'out-of-the-box' is inside __metamem.
Which means that I need to move the newFunc() method into the metamemory.

But then I didn't know how to access it from inside there, so I just exposed it with deff = __metatmem['deff']
(What is now called 'deff' (short for define function) used fo be called 'newFunc' here and 'defnew' in the MetaHelper)
'''