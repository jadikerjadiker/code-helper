import random

class World():
    '''
    this is the world that the babies are born into. It keeps track of
    all the new babies and deals with the birthing rate after they are born
    the gender babies should be when they are born
    how many people have been born
    the birthing age (what age people are when they start giving birth)
    the death age (what age people die at)
    the birth rate
    '''
    def __init__(self):
        self.newBabies = []
        self.allPeople = []
        self.gender = 1
        self.birthingAge = 10
        self.deathAge = 30
        self.personCounter = 0
        self.birthRate = 1/3
    
    def makeNewBaby(self):
        self.newBabies.append(Person(self))
        self.personCounter += 1

    def newYear(self):
        numOfBabies = self.doBabyCheck()
        self.makeBabies(numOfBabies)
        self.failBirths()
        self.makeEveryoneOlder()
        self.addNewBirthsToPop()
    
    def makeBabies(self, num):
        for i in range(num):
            self.makeNewBaby()
    
    def doBabyCheck

class Person():
    '''
    This is an individual person. It keeps track of its:
    name
    age
    gender
    world that it lives in
    whether or not it's alive
    whether or not it can give birth
    '''
    def __init__ (self, world):
        self.world = world
        self.name = "person"+str(self.world.personCounter)
        self.age = 0
        self.isAlive = True
        self.gender = world.gender
        #1 is male, 0 is female
        world.gender = (world.gender + 1)%2
        self.isBirthingAge = False
        
        
    def ageByOne(self):
        self.age = self.age+1
        self.update()
    
    def update(self):
        if self.age>=world.birthingAge:
            self.isBirthingAge = True
        if self.age>=world.deathAge:
            self.isAlive = False
            
    def getInfo(self):
        print("My name is {}, I am a {}, I am {} years old. Alive = {}, birthing = {}".format(self.name, self.gender, self.age, self.isAlive, self.isBirthingAge))
            