import re

def newFunc():
    global _mem
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