'''
#so first I need a representation of the board. I'm going to use a list with 25 slots
#actually, first I need to make a new environment for this project

clear environments()

Environments cleared

new env('Lazer Maze Solver')

Lazer Maze Solver environment created

new class('Board')

Would you like to make a new environment for this class?

Y #it's asking a yes or no question, so it is only looking for certain responses; no checks for envirovalues

With the same name?

Y

Board environment created
Is this a subclass?

N

What properties would you like this class to have?

'board' is an empty list #Oh no. How is it supposed to tell that I mean 'is an' which means '=' and empty list which means '[]' are separate? Hmph. I don't want to get caught in the same trap I was last year.

Would you like to make 'board' (which will return 'self.board') a property of the environment as well?

Y

Would you always like to make it a property of the environment (for this environment)?

Y

What should the property be called?

'board'

Would you always like it to have the same name?

Y

#most of this stuff should be stored in settings, that's a little too much communication.

What other properties would you like to add to the class?

 #here, I also want to have it create code that will add 25 open slots to the list
incom(new command('addSlotsToList', 'DynamicEnvironment')) #incom is short for insert command to tell the shell that I want to do this and then return back to the other command it's running (new class() in this case)

Define the method addSlotsToList:

incom(new command('forloop', 'DynamicEnvironment'))

Define the method 'forloop':

incom(new command('tabIn', 'DynamicEnvironment'))

Define the method 'tabIn':

(string):
    return string.replace('\n', '\n\t')
    
Method 'tabIn' defined in the environment 'DynamicEnvironment'.
Define the method 'forloop':

(howManyTimes, inside, indexIdentifier):
    if not indexIdentifier:
        indexIdentifier = 'i'
    return 'for '+indexIdentifier+' in range('+howManyTimes+'):\n\t'+tabIn(inside)
    
Method 'forloop' defined in the environment 'DynamicEnvioronment'.
Define the method addSlotsToList:

(listName, howMany):
    forloop(howMany, listName+'.append(None)')
    
Method addSlotsToList defined in the environment 'DynamicEnvironment'.
What other properties would you like to add to the class?

incom(addCode(addSlotsToList(board, 25)))

#So at this point, the response it's building up should look something like

#class Board():
    def __init__(self):
        self.board = []
        for i in range(25):
            self.board.append(None)
#I've had to type a lot in order to be able to set this up, but if it was already set up for me, then all I would have had to type at this point is
#new class 'Board'
#board is an empty table
#incom(addCode(addSlotsToList(board, 25))

Code added.
What other properties would you like to add to the class?

Done.

Here's your class:
class Board():
    def __init__(self):
        self.board = []
        for i in range(25):
            self.board.append(None)


#Let's try to make the piece class then

unload environment('Board')

'Board' environment unloaded successfully.
Type any command.

#assuming that those things I set up earlier are now saved for me in settings variables
new class('Piece')
#oops, I forgot that classes are initialized with variables. We'll add that in this one.

Is this class a subclass of anything (If so, type the subclass name in quotes)?
N

How would you like this class to be initialized?

("myType", "position = '?'", "direction = '?'")


What properties would you like this class to have?

normal properties ('type', 'pos', 'direction') #this will set self.type to myType, self.pos to position, etc.
#How would I program this function in?
#It would need to have access to the initialization thing. How would I know where that's stored? Hm.
#That could be another parameter: what to store it under
#its seeming like these environments need a subenvironment for functions of the environment.
#Nah: If it's something that should be saved for later (that the user would use) But those are different things.
#Okay, so again it looks like I have some things I want the computer to be able to store,...
#but not have the user access unless they're using the functions provided within the environment.
'''