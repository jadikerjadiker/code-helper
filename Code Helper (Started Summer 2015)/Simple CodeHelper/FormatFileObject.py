'''
London Lowmanstone IV
FormatFileObject Class
Version 2.2
2/6/2016

spacing error fixed
'''

#I think it's another one of those info newlines, but I'm not sure why or how they work.
import JustGetReader
import Format1p0Loader

class FormatFileObject():
    def __init__(self, file):
        self.file = file
        with open(file) as f:
            self.openFile = f
            
            #set the format of the file
            #does not actually check that 
            self.formatVersion = "".join(f.readline().split()).lower()[6:] #cut out the whitespace and lowercase it all and then cut out the part that should say "format"
                
            if self.formatVersion == "1.0":
                self.formatInfo = Format1p0Loader.run(self.file)
    
    def getItem(self, itemInfo):
        if self.formatVersion == "1.0":
            if isinstance(itemInfo, list): #itemInfo is a list
                myItem = itemInfo[0]
            else:
                myItem = itemInfo
            
            return JustGetReader.run(myItem, self.file, self.formatInfo)
            
    def addItem(self, itemInfo):
        if self.formatVersion == "1.0":
            name = itemInfo[0]
            item = itemInfo[1]
    
            with open("SetterTester.txt", "r+") as f:
                old = f.read() #save the file
                f.seek(0)
                linecheck = None #just to init it into the loop
                while linecheck != "startinfo": #looking for the start of the info to insert the item
                    line = f.readline()
                    if line=="":
                        raise IOError("FormatFileObject:addItem: could not find beginning of info!")
                    
                    linecheck = ''.join(line.split()).lower() #cut out all the whitespace and make all the letters undercase
                
                #poss update this takes up a lot of memory if the file is big
                endStuff = ""
                if line[-1]!="\n": #if the startinfo is at the end of the file
                    f.write("\n") #start us off on a new line
                else:
                    endStuff += "\n"
                where = f.tell() #save where the item should be inserted
                endStuff += f.read() #read in the rest of the file
                f.seek(where) #go back to where this should be inserted
                cacheInfo = self.formatInfo[0][0] #cache the part of the self.formatInfo that holds the info regarding the format around the name and value
                f.write(cacheInfo[0]+name+cacheInfo[1]+item+cacheInfo[2]+endStuff)
                return item
                