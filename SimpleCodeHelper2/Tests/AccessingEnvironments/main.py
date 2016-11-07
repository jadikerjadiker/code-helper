import importlib

'''
The goal is for the user to type in "ModuleName.EnvironmentName" and then it goes and loads the environment and prints out some attribute.

'''

sentinel = "..."
inputText1 = '\n'.join(iter(raw_input, sentinel))
(modName, envName) = inputText1.split(".")
print(modName, envName)
newMod = importlib.import_module(modName)
e = getattr(newMod, envName)()
print(e.name)

#alright, this works! e is an instantiated version of the environment.

