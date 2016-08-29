import importlib

class Shell1StaticEnvironment():
    def __init__(self):
        self.shellEnv = None #mainly so that the text editor will stop telling me I have errors when I don't

    #envName is a string in the form ModuleName.EnvironmentName or just EnvironmentName if its in the default module
    def loadExternalEnvironment(self, envPathName):
        myShell = self.shellEnv #cache
        if envPathName.find(".")!= -1: #if envPath has both a module and environment name
            (modName, envName) = envPathName.split(".")
            fullEnvName = envPathName
        else: #comes from default
            modName = myShell.internalDynamicEnv.defaultModule
            envName = envPathName
            fullEnvName = modName+"."+envName
        newEnv = getattr(importlib.import_module(modName), envName)()
        myShell.externalEnvs.append(newEnv)
        myShell.externalEnvPaths.append(fullEnvName)
        myShell.linkEnv(newEnv)