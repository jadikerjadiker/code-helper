class IllegalMove(RuntimeError):
        pass

class ChopsticksGame:
    def __init__(self, trackTies = True, repeatsBeforeTie = 2):
        self.game = [[1, 1], [1, 1]]
        self.currentPlayer = 0
        self.trackTies = trackTies
        
        #I have it initialize these fields so it doesn't throw an error if someone accidentally updates the positions
        self.positions = {} #dictionary where the keys are the string representations of the game, and the values are how many times that position has occured.
        self.repeatsBeforeTie = repeatsBeforeTie
        if trackTies:
            self.updatePositions() #make sure the initial position is stored
        
    def __str__(self):
        return "({}:{})".format(self.currentPlayer, self.game.__str__())
    
    #makes a move in the game, prints the game (if printGame is True), runs self.printGameEndState (if printGameEnd is True), and then returns the value of gameOver
    def moveAndPrint(self, printGame, printGameEnd, *args):
        end = self.moveAndCheck(*args)
        if printGame:
            print(self)
        if printGameEnd:
            self.printGameEndState(end)
        return end
        
        
    
    #makes a move in the game and then returns the value of self.gameOver()
    def moveAndCheck(self, *args):
        self.move(*args)
        return self.gameOver()
    
    #makes a move in the game. If the move is illegal it raises an IllegalMove exception. Does not return anything.    
    def move(self, *args):
        if len(args)<=1: #player is splitting
            if len(args)==0: #the player is set to be self.currentPlayer
                playerNum = self.currentPlayer
            else: #they specify the player (no check is done to make sure it's the currentPlayer). self.currentPlayer is still updated to be the opposite player.
                playerNum = args[0]
            
            thePlayer = self.getPlayer(playerNum)
            firstHandVal = thePlayer[0]
            secondHandVal = thePlayer[1]
            #check for illegal moves
            if (firstHandVal==0 and secondHandVal==0): #this should never happen because then the other person would have won, but it should be checked for anyway
                raise IllegalMove("Cannot split: both hands of player {} are out. Here's the game: {}".format(playerNum, self))
            if (firstHandVal!=0 and secondHandVal!=0):
                raise IllegalMove("Cannot split: both hands of player {} are still in. Here's the game: {}".format(playerNum, self))
            #now we know that one is 0 and the other is not, so we can add the two together to get the nonzero one.
            splitVal = (firstHandVal + secondHandVal)/2.0
            if splitVal%1!=0:
                raise IllegalMove("Cannot split: player {}'s hand is not an even number. Here's the game: {}".format(playerNum, self))
            #make the split and set the next player
            splitVal = int(splitVal)
            thePlayer[0] = splitVal
            thePlayer[1] = splitVal
        else: #player is doing a normal move
            if len(args)==3: #they specify the player (no check is done to make sure it's the currentPlayer). self.currentPlayer is still updated to be the opposite player.
                playerNum = args[0]
                ownHand = args[1]
                targetHand = args[2]
            elif len(args)==2: #the player is set to be self.currentPlayer
                playerNum = self.currentPlayer
                ownHand = args[0]
                targetHand = args[1]
            
            #check to make sure the move is legal, then make it and update self.currentPlayer
            otherP = self.getOtherPlayer(playerNum)
            myVal = self.getPlayer(playerNum)[ownHand]
            otherVal = otherP[targetHand]
            if myVal!=0 and otherVal!=0:
                otherP[targetHand] = self.add(myVal, otherVal)
            else: #One of the hands is zero - illegal move!
                if myVal==0:
                    exList = [ownHand, playerNum]
                else: #otherVal==0
                    exList = [targetHand, self.getOtherPlayerNum(playerNum)]
                
                exStr = "Cannot make the move {}: Hand number {} of player number {} is zero. Here's the game: {}".format((playerNum, ownHand, targetHand), exList[0], exList[1], self)
                raise IllegalMove(exStr)
        
        self.nextTurn()
        if self.trackTies:
            self.updatePositions()
        
    def add(self, toAdd, target):
        return (target+toAdd)%5        
        
    def getPlayer(self, num):
        return self.game[num]
        
    def getOtherPlayer(self, num):
        return self.getPlayer(self.getOtherPlayerNum(num))
        
    def getOtherPlayerNum(self, num):
        return (num+1)%2
        
    def nextTurn(self):
        self.currentPlayer = self.getOtherPlayerNum(self.currentPlayer)
    
    def updatePositions(self):
        stringyGame = self.game.__str__()
        try: #the position has occured one more time
            self.positions[stringyGame]+=1
        except KeyError: #the position has never occured yet
            self.positions[stringyGame] = 1
            
        
    def checkForTie(self):
        for aGame, howManyTimes in self.positions.iteritems():
            if howManyTimes>=self.repeatsBeforeTie:
                #print("The game {} has occured {} times.".format(aGame, howManyTimes))
                return True
        return False
    
    #the parameter 'state' should be whatever self.gameOver returns, or none if it should just be computed.
    #This function prints a human-readable version of who has won or it it's a tie. Prints nothing if the game is not over. 
    def printGameEndState(self, state = None):
        if state==None:
            state = self.gameOver()
        if state: #game is over (tie or player won)
            if isinstance(state, bool): #tie game
                print("Tie Game!")
            else: #player won
                print("Player {} won!".format(state))
    
    #If the game is over, it returns the number of the player that won or True (if the game was a tie). Otherwise returns False.
    def gameOver(self):
        for i in range(2):
            if self.game[i] == [0, 0]:
                return self.getOtherPlayerNum(i)
        if self.trackTies:
            if self.checkForTie():
                return True
        return False
        
#just some testing

'''        
c = ChopsticksGame(False, repeatsBeforeTie = 2)
def pmove(*args):
    c.move(*args)
    print(c)
    dispWinner()

def p():
    print(c)

def dispWinner():
    winner = c.gameOver()
    if winner:
        if type(winner) == 'number':
            print("Player {} won!".format(winner))
        else:
            print("Tie Game!")

def upPos():
    c.updatePositions()

upPos()
dispWinner()
print("Should have been nothing")
upPos()
dispWinner()
'''
