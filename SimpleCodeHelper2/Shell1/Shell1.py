import re

class InvalidCommand(RuntimeError):
    pass
    
class Shell1():
    def __init__(self):
        import Shell1StaticEnvironment
        self.internalStaticEnv = Shell1StaticEnvironment.Shell1StaticEnvironment()
        self.internalStaticEnv.shellEnv = self
        
        import Shell1DynamicEnvironment
        self.internalDynamicEnv = Shell1DynamicEnvironment.Shell1DynamicEnvironment()
        self.internalDynamicEnv.shellEnv = self
        
        #The first external environments that are loaded (in indexes 0, 1, etc.) are the last ones to be checked for commands.
        #self.externalEnvs and externalEnvPaths are linked lists, one containing the environments and the other containing the names
        self.externalEnvs = []
        self.externalEnvPaths = []
    
    #just sets the shellEnv property of thing to self
    def linkEnv(self, env):
        setattr(env, "shellEnv", self) #forces every loaded environment to have a shellEnv attribute that points to its parent shell
    
    #if you paste something in with the sentinel followed by a newline, it will immediately return everything up to that sentinel,...
    #and then append what came after it onto the next time it runs getCommand.
    #So if it contains the sentinel twice, this might try to run two commands before the user has a chance to react.
    def getCommand(self):
        return '\n'.join(iter(raw_input, self.internalDynamicEnv.inputSentinel))
    
    #gets the actual value of valString from the environments
    #this will check the static internal shell first, then the the external environments, and then the dynamic internal environment.
    def getEnvirovalue(self, valString):
        
        #check actual shell first
        try:
            return getattr(self, valString)
        except AttributeError:
            #check external environments, from most recently loaded to initially loaded
            for _, env in reversed(self.externalEnvs):
                try:
                    return getattr(env, valString)
                except AttributeError:
                    pass
            #check internal env
            try:
                return getattr(self.internalEnv, valString)
            except AttributeError:
                raise AttributeError("Attribute '{}' not found in environments.".format(valString))
    
    def runCommand(self, commandString):
        try:
            #group the stuff leading up to the first open parethensis and then...
            #make a second group of the stuff following that first parenthesis up until...
            #the last closing parenthesis and the end of the command
            (commandName, commandArgs) = re.match(r"^([^\(\)]+)\((.*)\)\s*$", commandString).groups()
        except AttributeError: #the command wasn't in the correct format, so it had no groups
            raise InvalidCommand("Sorry, your command '{}' was not in the right format.".format(commandString))
            
        print("Here was the commandName: {}".format(commandName))
        print("Here were the arguments: {}".format(commandArgs))

        try:
            command = self.getEnvirovalue(commandName) #todo finish this
        except AttributeError:
            raise InvalidCommand("Sorry, your command '{}' was not recognized by the current environments.".format(commandName))
        
        
        #todo go through the commandArgs and look for environment stuff to replace it.
        #todo deal with the parentheses inside the commandArgs
        
    def run(self):
        while True:
            command = self.getCommand()
            try:
                self.runCommand(command) #getCommand() returns a string, self.runCommand either runs the command or raises InvalidCommand
            except InvalidCommand as e:
                print(e) #print the invalid command message
                
        
        

if __name__ == "__main__":
    shell = Shell1()
    shell.run()