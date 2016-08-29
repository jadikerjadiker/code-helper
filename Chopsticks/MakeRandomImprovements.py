'''
The goal of this file is to create a neural net that wins 70% of the time against a random neural net.

If that can be achieved, I'll move onto a higher target.

The neural nets will be randomly created at the start, and play within themselves.
Then, the highest scoring ones will be kept, and if they get above a certain score, they will be tested to check for a winner.
If there is a winner, it will be returned so that the human can play some games against it (its weights and biases will also be printed out)
If not, the top scorers will have multiple slightly mutated nets put into the pool, retaining the originals, and the lower scoring ones will be removed.
Then, more random nets will be generated to fill up the rest of the slots in the pool.
Rinse and repeat.
'''

import random
import numpy as np
import MyNeuralNet as mnn
import ChopsticksGame as cg
import NeuralToChopsticks as ntc
import RandomPlayers as rp

'''
neuralTopology = [4, 5, 6, 5] #how many neurons are in each layer
poolSize = 800 #how many nets are in the pool
lossGoalPc = .1 #target percentage of how often it should not lose against a completely random player
winGoalPc = .7 #target percentage of how often it should win against a completely random player
goalGamesToPlay = 100 #how many games it plays when determining whether a net passes the goal
gamesPerRound = 50 #how many games are played against random nets in the pool in order to determine a score for the round
scoring = [1, 0, -3] #[winPoints, tiePoints, losePoints]
keep = 7 #how many top players should be kept and mutated
mutateFactor = 100 #how many mutated versions should be put into the pool per original good net? (including originals) Must be >= 1.

#percentages here are 1 = 100%
#Pcs is short for "percentages"
mutationAmtPcs = 98*[1] + 2*[2] #list of how many mutations a net will get. A number is chosen randomly out of the list.
changeTopologyPc = .001 #chance that a mutation will cause a change in topology
addNeuronsPc = .007 #chance that a neuron will be added during a topology mutation (otherwise a neuron will be removed)
changeWeightPc = .6 #change that a weight will be changed instead of a bias
neuronAmtPcs = [1] #list of how many neurons should be added or subtracted in one mutation. A number is chosen randomly out of the list.

#when a weight is changed by a random number (from the normal distribution, I believe),
#it will be multiplied by a number from this list (weightChangeMagnitudePcs) before being added or subtracted from a current weight
weightBiasChangeMagnitudePcs = 49*[.1] + 1*[.3]
weightAmtPcs = 89*[1]+10*[2]+1*[3] #list of how many weights will be changed in one mutation. A number is chosen randomly out of the list.
'''

class CompetitionNet(mnn.NeuralNet):
    def __init__(self, neuronAmts, weights = None, biases = None):
        '''
        print("Making a new competition net. Here's what I got for neuronAmts, weights and then biases")
        print(neuronAmts)
        print(weights)
        print(biases)
        '''
        mnn.NeuralNet.__init__(self, neuronAmts, weights, biases)
        self.score = 0
        
    def copy(self):
        return CompetitionNet(self.neuronsPerLayer, self.weights, self.biases)
        

def makeRandomImprovements(neuralTopology = [4, 5, 6, 5], poolSize = 800, lossGoalPc = .1, winGoalPc = .4, goalGamesToPlay = 100, gamesPerRound = 50, scoring = [1, 0, -3],
                            keep = 7, mutateFactor = 100, mutationAmtPcs = 98*[1] + 2*[2], changeTopologyPc = .001, addNeuronsPc = .007, changeWeightPc = .6,
                            neuronAmtPcs = [1], weightBiasChangeMagnitudePcs = 50*[.1] + 1*[.3], weightBiasAmtPcs = 89*[1]+10*[2]+1*[3]):
    
    #returns the score of a net, used when sorting
    def getScore(net):
        return net.score
        
    def addRandomsToPool(pool, amt):
        for i in range(amt):
            pool.append(CompetitionNet(neuralTopology)) #add random nets to the pool
    
    #plays a round of games and sorts the pool of neural nets by who got the best scores during that round.
    def doRound():
        #I'm going to make a score property for them and then sort the pool based on that score property.
        poolSize = len(pool) #printable
        incrementAmt = 100.0/poolSize
        logPercentAmt = 2
        roundAmt = 2
        #print("incrementAmt:"+str(incrementAmt))
        for netIndex, net in enumerate(pool):
            #commenting out the code that made it play against other nets in the pool. Now just going to have it play against a random player
            possOpponentIndexes = range(poolSize) #create a list of all the possible opponents
            possOpponentIndexes.pop(netIndex) #Don't want it to play itself
            random.shuffle(possOpponentIndexes) #randomize who it plays against.
            
            for gameNum in range(gamesPerRound):
                opponentIndex = possOpponentIndexes.pop() #get an opponent to play and remove that opponent from the list
                net.score+=scoring[playGame(net, pool[opponentIndex])] #changes the score based on the outcome of the game
            
            
            
            for gameNum in range(gamesPerRound):
                
                '''
                #Allows the human to occasionally view games played by whatever net it's on.
                if random.random()<.00001:
                    import VerboseGames
                    res = VerboseGames.computerVComputerGame(net.copy, rp.makeRandomPlayer)
                '''
                res = playGame(net, randomPlayer)
                net.score+=scoring[res]
            
            
            printPc = 100.0*(netIndex+1)/poolSize #todo finish
            if printPc%logPercentAmt<incrementAmt:
                print("{}%...".format(round(printPc, roundAmt)))
            
        pool.sort(key = getScore, reverse = True) #sorts the pool based on the score of the neural nets
    
    #plays a game between net1 and net2 and returns the index of the score that net1 should get on the game (0 if it won, 1 for a tie, 2 for a loss)
    def playGame(net1, net2):
        def randBool():
            return random.random() < 0.5
        
        c = cg.ChopsticksGame(repeatsBeforeTie = 3) #if it reaches the same board position twice, it should call it a tie.
        h = ntc.NeuralToChopsticks(c)
        isFirstPlayer = randBool() #True if the main net goes first, false otherwise
        curTurn = isFirstPlayer
        gameDone = False
        
        while isinstance(gameDone, bool) and gameDone==False: #without the isinstance it might think 0==False and not stop when player 0 wins
            if curTurn: #The main net's turn
                h.haveNetMakeMove(net1)
            else: #The other net's turn
                h.haveNetMakeMove(net2)
            gameDone = c.gameOver() #True if the game is a tie, 0 if the player taking the first turn won
            curTurn = not curTurn #change who's turn it is
                
        if isinstance(gameDone, bool) and gameDone==True:
            return 1
        elif gameDone==0:
            if isFirstPlayer:
                return 0
            else:
                return 2
        else: #gameDone==1
            if not isFirstPlayer:
                return 0
            else:
                return 2
    
    #sets up the next pool with mutated and random nets best on the top nets
    def nextPool(pool):
        def addMutationSet(baseNet):
            #upgrade: make changeWeight and changeBias be actually random...
            #(instead of randomly picking a layer and then choosing one from within that layer, it should randomly pick one in general)
            def getBoolFromPc(pc):
                return random.random() < pc
            
            #chooses a random layer and changes a random weight by amt within that layer.
            def changeWeight(amt):
                layerNum = random.randint(1, len(mutNet.neuronsPerLayer)-1) #number of the layer that the changed weight will be in
                layer = mutNet.weights[layerNum]
                layerShape = layer.shape
                #pick a random weight in the layer to change and change it
                layer[random.randint(0, layerShape[0]-1)][random.randint(0, layerShape[1]-1)] += amt
            
            #chooses a random layer and changes a random bias by amt within that layer.
            def changeBias(amt):
                #choose a random layer, and then a random bias, and then change it by amt.
                layerNum = random.randint(1, len(mutNet.neuronsPerLayer)-1)
                layer = mutNet.biases[layerNum]
                mutNet.biases[layerNum][random.randint(0, layer.shape[0]-1)][0] += amt
                
                
            #adds a neuron to the top of a random layer in the net to be mutated   
            def addNeuron():
                maxLayer = len(mutNet.neuronsPerLayer)-2
                if maxLayer>=1:
                    #upgrade: repeated code here
                    layerNum = random.randint(1, len(mutNet.neuronsPerLayer)-2) #layer that the neuron will be added to
                    oldNpl = mutNet.neuronsPerLayer #short for 'Old NeuronsPerLayer'
                    mutNet.neuronsPerLayer[layerNum]+=1
                    mutNet.weights[layerNum] = np.append(mutNet.weights[layerNum], np.random.randn(1, oldNpl[layerNum-1]), axis = 0)
                    mutNet.weights[layerNum+1] = np.append(mutNet.weights[layerNum+1], np.zeros((oldNpl[layerNum+1], 1)), axis = 1)
                    mutNet.biases[layerNum] = np.append(mutNet.biases[layerNum], np.random.randn(1, 1), axis = 0)
            
            #chooses a random layer and removes a neuron from it.
            #If a layer only has one neuron, or there are no intermediate layers, this does nothing.
            def removeNeuron():
                maxLayer = len(mutNet.neuronsPerLayer)-2
                if maxLayer>=1:
                    layerNum = random.randint(1, len(mutNet.neuronsPerLayer)-2)
                    neuronsInLayer = mutNet.neuronsPerLayer[layerNum]
                    if neuronsInLayer>1:
                        neuronNum = random.randint(0, neuronsInLayer-1)
                        mutNet.weights[layerNum] = np.delete(mutNet.weights[layerNum], neuronNum, axis = 0)
                        mutNet.weights[layerNum+1] = np.delete(mutNet.weights[layerNum+1], neuronNum, axis = 1)
                        mutNet.biases[layerNum] = np.delete(mutNet.biases[layerNum], neuronNum, axis = 0)
            
            #upgrade: failed mutations (taking away a layer when there is none to be taken) should result in a different mutation, not just silently fail.
            #run addMutationSet()
            for i in range(mutateFactor-1): #for each mutated net that should be made
                mutNet = baseNet.copy() #copy the baseNet so the new net can be mutated
                
                #a mutation consists of either 1. Adding or removing neurons or 2. Changing weights or biases
                mutationAmt = random.choice(mutationAmtPcs) #how many mutations will be made to the original net in order to make this new one
                for mutationNum in range(mutationAmt):
                    if getBoolFromPc(changeTopologyPc): #changing the topology (adding or subtracting neurons)
                        neuronAmt = random.choice(neuronAmtPcs) #how many neurons to add or remove
                        if getBoolFromPc(addNeuronsPc): #adding neurons
                            for neuronNum in range(neuronAmt):
                                addNeuron()
                        else: #removing neurons
                            for neuronNum in range(neuronAmt):
                                removeNeuron()
                    else: #just changing weights and biases
                        #upgrade different magnitudes and amtPcs for weights versus vectors
                        #gets a random number (from the standard normal distribution) and then makes applies the magnitude factor
                        changeAmt = random.choice(weightBiasChangeMagnitudePcs)*np.random.randn()
                        weightBiasAmt = random.choice(weightBiasAmtPcs) #how many weights are going to be changed in this mutation
                        #upgrade: make sure it changes different weights each time
                        for weightNum in range(weightBiasAmt):
                            if getBoolFromPc(changeWeightPc): #changing a weight
                                changeWeight(changeAmt)
                            else: #changing a bias
                                changeBias(changeAmt)
                
                '''
                print("Add mutation set - got net:\n{}".format(baseNet))
                print("Add mutation set - gave back the net\n{}".format(mutNet))
                '''
                pool.append(mutNet)
        #run nextPool()
        keepers = pool[:keep] #list of all the nets that are being kept
        pool = pool[:keep] #reset the pool, keeping the good nets
        for baseNet in keepers:
            addMutationSet(baseNet) #add the correct number of mutation nets based off the baseNet
        addRandomsToPool(pool, randomNetAddAmt) #add the correct number of randoms to the pool
        #dp
        print("After resetting the pool, it now has {} nets in it".format(len(pool))) #printable
        return pool
        
    #returns a list of all the nets that passed the test        
    def checkForWinners():
        def testWinner(net):
            wins = 0.0
            losses = 0.0
            for j in range(goalGamesToPlay):
                res = playGame(net, randomPlayer)
                if res==0: #if it lost
                    wins+=1
                elif res==2:
                    losses+=1
            
            percentWon = round(wins*100/goalGamesToPlay, 2)        
            percentLost = round(losses*100/goalGamesToPlay, 2)
            print("Won: {}% Lost: {}%".format(percentWon, percentLost)) #printable
            if losses/goalGamesToPlay <= lossGoalPc and wins/goalGamesToPlay >= winsGoalPc: #see if the percentage is high enough to be a winner
                return True
            else:
                return False
                
            
        ans = []
        #Go through each of the nets that are worth keeping and see if they pass
        print("Checking for winners...") #printable
        for i in range(keep):
            testNet = pool[i]
            if testWinner(testNet):
                ans.append(testNet)
        print("There are the percentages of the top players for round #{}".format(roundNumber)) #printable
        for i, net in enumerate(pool):
            net.score = 0
        return ans #return the list of winners
    
    def getTopScores(): #printable
        ans = []
        for i in range(keep):
            ans.append(pool[i].score)
        return ans
            
    def printTopScores(): #printable
        print("Here are the top scores: {}".format(topScores))
        
    def printTopNet():
        print("The highest score was achieved by the following net:\n{}".format(pool[0]))
        
    #run
    #set up non-preference variables
    randomNetAddAmt = poolSize-keep*mutateFactor #how many random nets should be added to the pool
    randomPlayer = rp.makeRandomPlayer() #have a set player who makes completely random decisions
    pool = []
    
    addRandomsToPool(pool, poolSize) #initiates the pool with random nets
    roundNumber = 1 #printable
    print("Starting Round #{}!".format(roundNumber)) #printable
    doRound() #makes the pool into a sorted list of the best players (with the best at the front)
    topScores = getTopScores()
    printTopScores()
    winners = checkForWinners() #the list of neural nets that pass the test; empty if none passed.
    printTopNet()
    roundNumber+=1 #increase the round number
    while winners==[]:
        pool = nextPool(pool) #set up the next pool with mutated and random nets.
        print("Starting Round #{}!".format(roundNumber)) #printable
        doRound() #play rounds until it's done.
        printTopScores()
        winners = checkForWinners() #the list of neural nets that pass the test; empty if none passed.
        printTopNet()
        roundNumber+=1 #increase the round number
    return winners

'''
ann = CompetitionNet([4, 5, 6, 5])
ann2 = ann.copy()
print("1:\n{}\n\n2:\n{}".format(ann, ann2))
'''