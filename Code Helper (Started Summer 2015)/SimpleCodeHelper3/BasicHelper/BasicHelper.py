'''
Goal: Be able to teach it new functions that it can run.

Plan:
Have it eval the code that's put in. If it doesn't recognize a function, then have it crash.
One of the functions it recognizes inherently allows you to define a new function.
'''
'''
Upgrades:

Make it so that when I hit enter I can still go back and edit what I typed up to that earlier point.

Put "def " in the first line when defining a function so that I am forced to put my def right there.

Deal with people making mistakes. Allow them to redo stuff.

Make sure that's what's being added is one function. (Not needed until much later)

Have one file for new functions that are being added. That way you don't have to reimport everything every single time.

A way to delete functions, both from working and from the file. (http://stackoverflow.com/questions/26545051/is-there-a-way-to-delete-created-variables-functions-etc-from-the-memory-of-th)
'''

#todo run through the helper with the nonologix solver.

import re
import readline as rl

rl.parse_and_bind('set editing-mode vi') #allow for arrow keys to be used for raw_input.
rl.parse_and_bind("TAB: '    '") #set the tab key to make 4 spaces


_mem = {}
__metamem = {'sentinel':'.', 'userDefinedFile':'UserDefined.py'}

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
    
def _():
    global __metamem
    print("Define a new function here, and we'll add it. The sentinel is '{}'".format(__metamem['sentinel']))
    inputText = __metamem['getInput']()
    memsToAdd = ""
    if inputText.find('_mem')>=0:
        memsToAdd+="\tglobal _mem\n"
    if inputText.find('__metamem')>=0:
        memsToAdd+="\tglobal __metamem\n"
        
    #if something in the function probably uses _mem or __metamem,...
    #make sure that the global variable is used at the start of the function so that they're imported from the main module
    if inputText!="": 
        memoryIndex = inputText.find('\n')+1
        inputText = inputText[:memoryIndex]+memsToAdd+inputText[memoryIndex:]
    inputText = inputText.replace("\t", "    ") #make sure tabs are turned into four spaces like they should be.
    #upgrade: check to make sure only one function is being put in
    
    #checking to make sure the function is runnable
    try:
        _ = None #just to get rid of the IDE thinking that _ doesn't exist.
        funcName = re.search(r"def[ ]+?(\S+?)[ ]*?\(.*\)", inputText).group(1)
        exec(inputText) #this is very very dangerous
        exec('_ = '+funcName)
        if hasattr(_, '__call__'): #check if you actually did make a function
            with open(__metamem['userDefinedFile'], 'a') as f:
                f.write('\n\n'+str(inputText))
            print("The function '{}' was added.".format(funcName))
        else:
            raise RuntimeError
    except Exception as e:
        __metamem['printError'](e, "Couldn't make the function because '{}'")
__metamem['deff'] = _

if __name__ == "__main__":
    print("Give me something to do:")
    #todo I'm not sure that this really works how I want it to, but it seems to.
    deff = __metamem['deff'] #exposes it to the user
    while True:
        execfile(__metamem["userDefinedFile"])
        
        inputText = __metamem['getLineInput']('')
        print("\nRunning...\n")
        try:
            exec(inputText)
        except Exception as e:
            #print("Sorry, I didn't quite get that: {}".format(e.message))
            __metamem['printError'](e, "Sorry, I didn't quite get that because '{}'")
        
        __metamem['clearMemory']()
        print("\nGive me something else to do:")
        
