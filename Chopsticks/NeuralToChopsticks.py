import ChopsticksGame as cg
import numpy as np

class IllegalNeuralMove(cg.IllegalMove):
    pass

#In this code, I use 'net' to refer to the actual neural net (or its output),
#'Neural' to refer to the number system (1-5) that the net uses to make its move, and
#'Game' to refer to the list system that the chopstick game uses to make a move.

#returns true if the move worked, false if it didn't, and raises IllegalNeuralMove if it did not understand the move
class NeuralToChopsticks():
    def __init__(self, chopsticksGame = None):
        self.game = chopsticksGame
    
    def __str__(self):
        return self.game.__str__()
    
    def makeNeuralMove(self, num):
        try:
            self.game.move(*self.convertMoveFromNeuralToGame(num))
            return True
        except cg.IllegalMove:
            return False
            
    def convertMoveFromNeuralToGame(self, num):
        switcher = {
            1:[0, 0],
            2:[0, 1],
            3:[1, 0],
            4:[1, 1],
            5:[]
        }
        try:
            args = switcher[num]
            return args #give arguments that can be passed into the move function of the game
        except KeyError:
            raise IllegalNeuralMove("Unknown Neural Move: {}".format(num))
    
    #converts the output of the neural net into a list where the net's moves are in order of preference
    def convertMovesFromNetToNeural(self, colVec):
        vals = np.ndarray.tolist(colVec) #converts the output into a list of lists where each mini list contains one number
        for i, v in enumerate(vals):
            vals[i] = v[0] #take the numbers out of the unneeded lists.
            
        origList = list(vals) #store where the numbers were originally in order to keep track of what neuron they came from
        vals.sort(reverse = True) #we want biggest first
        for i, v in enumerate(vals):
            for i2, v2 in enumerate(origList):
                if v2==v:
                    vals[i] = i2+1 #replace the higher values with the neuron number that was giving them
                    break
        return vals        
    
    #makes a move in the game given the output from the net. Returns the neural number of the move it made.
    def makeMoveFromNet(self, output):
        moves = self.convertMovesFromNetToNeural(output)
        i = 0
        theMove = moves[i]
        while not self.makeNeuralMove(theMove):
            i+=1 #try the next move if the first does not work.
            try:
                theMove = moves[i]
            except IndexError:
                IllegalNeuralMove("Could not make a move from the moves list: {}. Here is the output I got: {}. Here is the game: {}.".format(moves, output, self.game))
        return theMove
    
    #takes a neural net and has it make a move in the game. Returns the move that it made.    
    def haveNetMakeMove(self, net):
        return self.makeMoveFromNet(net.run(self.convertGameToNet()))
    
    #uses self.game and converts the game into input for the neural net. Reverses the two players if player 1 is active. (That way the net always sees itself on the 'left')
    def convertGameToNet(self):
        g = self.game
        playerGoing = g.getPlayer(g.currentPlayer)
        playerWaiting = g.getOtherPlayer(g.currentPlayer)
        return [playerGoing[0], playerGoing[1], playerWaiting[0], playerWaiting[1]]
        
'''
c = cg.ChopsticksGame()
n = NeuralToChopsticks(c)

def pam(num): #short for printAllMove()
    n.game.moveAndPrint(True, True, *n.convert(num))
    
player = n.game.getPlayer(0)
player[0] = 0
player[1] = 4
pam(5)
player = n.game.getPlayer(1)
player[0] = 0
player[1] = 4
player = n.game.getPlayer(0)
player[0] = 0
player[1] = 0
pam(5)
'''

'''
c = cg.ChopsticksGame()
n = NeuralToChopsticks(c)
print(n)
print(n.convertGameToNet())
player = n.game.getPlayer(0)
player[0] = 0
player[1] = 4
print(n)
n.makeMoveFromNet(np.resize(np.array([6, .3, .5, .6, 5]), (5, 1)))
print(n)
'''

