import ChopsticksGame as cg
import MyNeuralNet as nn
import NeuralToChopsticks as ntc
import RandomPlayers as rp
import random

def humanVComputerGame(netSetupFunc = rp.makeRandomNet):
    computerPlayer = netSetupFunc()
    #print("Here is the net you are playing against:\n{}".format(computerPlayer))
    c = cg.ChopsticksGame(repeatsBeforeTie = 3) #short for 'chopsticks'
    h = ntc.NeuralToChopsticks(c) #short for 'helper'
    
    def goPlayer():
        try:
            playerMove = int(raw_input("Your turn! "))
        except KeyboardInterrupt:
            raise
        except:
            print("Sorry, I didn't understand that. Please type a whole number from 1 to 5. (See instructions above.)")
            return goPlayer()
        if playerMove<1 or playerMove>5:
            print("Sorry, I didn't understand that. Please type a whole number from 1 to 5. (See instructions above.)")
            return goPlayer()
        else: #player put in something that might work
            if not h.makeNeuralMove(playerMove): #if it didn't work
                print("Sorry, {} is an invalid move for this game position. Please try again.".format(playerMove))
                return goPlayer()
        
    def goComputer():
        compMove = h.haveNetMakeMove(computerPlayer)
        print("The computer made the move {}".format(compMove))
        
    def playAgain():
        ans = str(raw_input("Would you like to play again? (y/n) "))
        if ans == 'y':
            humanVComputerGame(netSetupFunc)
        elif ans == 'n':
            print("Goodbye!")
        else:
            print("I didn't understand that. Please type 'y' or 'n'.")
            return playAgain()
    
    print("Playing against a random neural net!")
    print("Instructions:")
    print("1: Active player uses left hand to hit opponent's left hand")
    print("2: Active player uses left hand to hit opponent's right hand")
    print("3: Active player uses right hand to hit opponent's left hand")
    print("4: Active player uses right hand to hit opponent's right hand")
    print("5: Split")

    #run
    gameDone = False
    while isinstance(gameDone, bool) and gameDone==False: #without the isinstance it might think 0==False and not stop when player 0 wins
        print(c.game)
        if c.currentPlayer == 0:
            goPlayer()
        else: #c.currentPlayer == 1
            goComputer()
        gameDone = c.gameOver()
        #print(c.positions)
        #print("gameDone: {}".format(gameDone))
        
    if isinstance(gameDone, bool) and gameDone==True:
        print("Tie Game")
    elif gameDone==0:
        print("Good job, human! You won!")
    else: #gameDone==1
        print("Too bad, the computer beat you!")
    
    return playAgain()
        
def computerVComputerGame(setupComp1Func, setupComp2Func, printStart = True):
    comp1 = setupComp1Func()
    comp2 = setupComp2Func()
    players = [comp1, comp2]
    c = cg.ChopsticksGame(repeatsBeforeTie = 4) #short for 'chopsticks'
    h = ntc.NeuralToChopsticks(c) #short for 'helper'

    def playAgain():
        ans = str(raw_input("Would you like to see another game? (y/n) "))
        if ans == 'y':
            print("-"*43)
            computerVComputerGame(setupComp1Func, setupComp2Func, printStart = False)
        elif ans == 'n':
            print("Thanks for watching!")
        else:
            print("I didn't understand that. Please type 'y' or 'n'.")
            playAgain()
    
    if printStart:
        print("Computers are playing against each other!")
        print("Moves:")
        print("1: Active player uses left hand to hit opponent's left hand")
        print("2: Active player uses left hand to hit opponent's right hand")
        print("3: Active player uses right hand to hit opponent's left hand")
        print("4: Active player uses right hand to hit opponent's right hand")
        print("5: Split")

    #run
    gameDone = False
    c.currentPlayer = random.randint(0, 1)
    print("New game!")
    while isinstance(gameDone, bool) and gameDone==False: #without the isinstance it might think 0==False and not stop when player 0 wins
        print(c.game)
        print("Player {} made the move {}".format(c.currentPlayer+1, h.haveNetMakeMove(players[c.currentPlayer])))
        gameDone = c.gameOver()
        
    if isinstance(gameDone, bool) and gameDone==True:
        print("Tie Game!")
    elif gameDone==0:
        print("Player 1 Won!")
    else: #gameDone==1
        print("Player 2 Won!")
    
    playAgain()
    
        
