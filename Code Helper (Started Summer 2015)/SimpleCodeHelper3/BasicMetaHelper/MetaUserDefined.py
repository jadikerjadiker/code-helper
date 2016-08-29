def defnew():
    global _mem
    global __metamem
    print("Define a new function here. The sentinel is '{}'".format(__metamem['sentinel']))
    inputText = __metamem['getInput']()
    with open(__metamem['userDefinedFile'], 'a') as f:
        memoryIndex = inputText.find('\n')+1
        inputText = inputText[:memoryIndex]+"\tglobal _mem\n\tglobal __metamem\n"+inputText[memoryIndex:] #make sure the memory and metamemory are imported from the main module
        inputText = inputText.replace("\t", "    ") #make sure tabs are turned into four spaces like they should be.
        #upgrade: check to make sure only one function is being put in
        #I'm just checking to make sure the function is runnable
        try:
            _ = None #just to get rid of the IDE thinking that _ doesn't exist.
            funcName = re.search(r"def[ ]+?(\S+?)[ ]*?\(.*\)", inputText).group(1)
            exec(inputText) #this is very very dangerous
            exec('_ = '+funcName)
            if hasattr(_, '__call__'): #check if you actually did make a function
                f.write('\n\n'+str(inputText))
                print("The function '{}' was added.".format(funcName))
            else:
                raise RuntimeError
        except Exception as e:
            __metamem['printError'](e, "Couldn't make the function because '{}'")

def tab(s):
    return '\t'+s.replace("\n", "\n\t")

def spacetab(s):
    return s.replace("\n", "\n    ")

def defNew():
    defnew()

def forloop(num):
    return spacetab("for i in range({}):\n\t".format(num))

def enumThroughTable(tblName):
    return spacetab("for i, val in enumerate({}):\n\t".format(tblName))

def p(something):
    print(something)

def deffMetaFunc(name, funcBody):
    paramEnd = funcBody.find('\n')
    return "def _{}:\n".format(funcBody[:paramEnd])+tab(funcBody[paramEnd+1:])+"\n__metamem['{}'] = _".format(name)