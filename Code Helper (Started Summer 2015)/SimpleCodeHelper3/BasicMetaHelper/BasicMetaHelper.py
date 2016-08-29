'''
Goal: Be able to teach it new functions that it can run.

Plan:
Have it eval the code that's put in. If it doesn't recognize a function, then have it crash.
One of the functions it recognizes inherently allows you to define a new function.
'''
'''
Upgrades:

Make it so that when I het enter I can still go back and edit what I typed up to that earlier point.

Put "def " in the first line when defining a function so that I am forced to put my def right there.

Deal with people making mistakes. Allow them to redo stuff.

Make sure that's what's being added is one function. (Not needed until much later)
'''

import re

_mem = {}
__metamem = {'sentinel':'.', 'userDefinedFile':'MetaUserDefined.py', 'externalImports':['re']}

#add certain useful functions to the metamemory.
def _(sentinel = __metamem['sentinel']):
    return '\n'.join(iter(raw_input, sentinel))
__metamem['getInput'] = _

def _(prompt = ''):
    return raw_input(prompt)
__metamem['getLineInput'] = _

def _():
    _mem = {}
__metamem['clearMemory'] = _

def _(e, s = "Error: {}"): #deal with an exception, where the exception's name is @param n and the string you want to be formatted with the error is s. @param m is the working message
    if e.message:
        m = e.message
    else:
        m = e.__doc__
    print(s.format(m))
__metamem['printError'] = _
    


if __name__ == "__main__":
    print("MetaHelper")
    print("Give me something to do:")
    while True:
        execfile(__metamem["userDefinedFile"])
        
        inputText = __metamem['getLineInput']('')
        print("\nRunning...")
        try:
            exec(inputText)
        except Exception as e:
            #print("Sorry, I didn't quite get that: {}".format(e.message))
            __metamem['printError'](e, "Sorry, I didn't quite get that because '{}'")
        
        __metamem['clearMemory']()
        print("\nGive me something else to do:")