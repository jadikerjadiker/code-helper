import numpy as np
import ChopsticksGame as cg
import NeuralToChopsticks as ntc
import MyNeuralNet as mnn
import RandomPlayers as rp
import random

'''
This module should have a function that takes a neural net and has it play against x number of random neural nets (or random players in general), and then records how many it won or lost (and the percentages)
'''
        
def neuralVRandom(theNet, gamesToPlay, printOut = False, shouldScore = False, lossScore = 0, tieScore = 0, winScore = 0, totallyRandom = False):
    def randBool():
        return random.random() > 0.5
    
    stats = [0, 0, 0] #[wins, ties, losses] 

    for i in range(gamesToPlay):
        if totallyRandom:
            rep = 2 #repeatsBeforeTie
        else:
            rep = 2
        c = cg.ChopsticksGame(repeatsBeforeTie = rep)
        h = ntc.NeuralToChopsticks(c)
        isFirstPlayer = randBool()
        curTurn = isFirstPlayer
        gameDone = False
        
        #remake a new neural net
        if totallyRandom:
            otherNet = rp.RandomPlayer()
        else:
            otherNet = mnn.NeuralNet([4, 5, 6, 5])

        while isinstance(gameDone, bool) and gameDone==False: #without the isinstance it might think 0==False and not stop when player 0 wins
            if curTurn: #The net's turn
                h.haveNetMakeMove(theNet)
            else: #The random player's turn
                h.haveNetMakeMove(otherNet)
            gameDone = c.gameOver()
            curTurn = not curTurn
                
        if isinstance(gameDone, bool) and gameDone==True:
            stats[1]+=1
        elif gameDone==0:
            if isFirstPlayer:
                stats[0]+=1
            else:
                stats[2]+=1
        else: #gameDone==1
            if not isFirstPlayer:
                stats[0]+=1
            else:
                stats[2]+=1
    if shouldScore:
        score = stats[0]*lossScore+stats[1]*tieScore+stats[2]*winScore
    else:
        score = None
    if printOut:        
        print("Won: {} ({}%)\nTied: {} ({}%)\nLost: {} ({}%)".format(stats[0], int(100*stats[0]/gamesToPlay), stats[1], int(100*stats[1]/gamesToPlay), stats[2], int(100*stats[2]/gamesToPlay)))
        if shouldScore:
            print("Score: {}".format(score))
        print("") #print a blank line for separation
            
    return (stats, score)
            
def neuralVRandomEpoch(setupPlayerFunc, gamesToPlay, epochs, printOut = True, printOutMini = False, shouldScore = False, lossScore = 0, tieScore = 0, winScore = 0, totallyRandom = False):
    maxScore = False
    avgScore = 0
    stats = [0, 0, 0] #[averageWinsPerEpoch, averageTiesPerEpoch, averageLossesPerEpoch]
    for i in range(epochs):
        smallStats, score = neuralVRandom(setupPlayerFunc(), gamesToPlay, printOutMini, shouldScore, lossScore, tieScore, winScore, totallyRandom)
        if shouldScore:
            if score>maxScore or isinstance(maxScore, bool):
                maxScore=score
            avgScore+=score
        stats = [x + y for x, y in zip(stats, smallStats)] #add up each game to the total stats
        if printOut:
            print("{}%...".format(round(100.0*(i+1)/epochs, 1)))
    
    stats = [1.0*x/epochs for x in stats]
    percents = [int(round(100.0*x/gamesToPlay)) for x in stats]
    if shouldScore:
        avgScore/=epochs
    if shouldScore:
        tackOn = " Average Score: {} Max Score: {}".format(avgScore, maxScore)
    else:
        tackOn = ""
    if printOut:
        print("Averages: Won: {} ({}%) Tied: {} ({}%) Lost: {} ({}%)".format(stats[0], percents[0], stats[1], percents[1], stats[2], percents[2])+tackOn)
        print("")
    
#neuralVRandom(mnn.NeuralNet([4, 5, 6, 5]), 1000) #50% winning is possible, but %60 percent is unheard of and %70 would be a fantastical target.
#neuralVRandom(mnn.NeuralNet([4, 6, 5]), 1000, True, True, 1, 0, -1, True) # 60% gotten about 1/20. 50% happens about 1/10... maybe mutations could also remove a neuron or a layer?
#neuralVRandomEpoch([4, 5, 6, 5], 100, 50, True, False, True, 1, 0, -1, True) #Usually get a negative score less that -10
#neuralVRandomEpoch([4, 6, 5], 100, 1000, True, False, True, 1, 0, -1, True) #Averages: Won: 37.949 (38%) Tied: 4.774 (5%) Lost: 57.277 (57%) Average Score: -20 Max Score: 44
#neuralVRandomEpoch([4, 5, 6, 5], 100, 1000, True, False, True, 1, 0, -1, True) #Averages: Won: 36.565 (37%) Tied: 4.897 (5%) Lost: 58.538 (59%) Average Score: -22 Max Score: 37
#neuralVRandomEpoch([4, 5, 5, 5], 50, 1000, True, False, True, 1, 0, -1, True) #Averages: Won: 17.842 (36%) Tied: 2.322 (5%) Lost: 29.836 (60%) Average Score: -12 Max Score: 20
#In short, this will be interesting.

#I think I made a mistake and reversed who won and lost, so I'm going to redo it and see if the results are reversed.
#neuralVRandomEpoch([4, 5, 5, 5], 50, 1000, True, False, True, 1, 0, -1, True) #Averages: Won: 29.182 (58%) Tied: 2.469 (5%) Lost: 18.349 (37%) Average Score: 10 Max Score: 43
#So yes, now it is flipped. It's scary how much I trusted its response before. I wonder why it wins more than a random one.
#I'm going to go back and double check that I really am doing it right this time. It seems like it is. This is really weird.
#Well then, if I have random nets play random nets, it should be about equal, right?
#neuralVRandomEpoch([4, 5, 5, 5], 50, 1000, True, False, True, 1, 0, -1, False) #Averages: Won: 17.901 (36%) Tied: 14.041 (28%) Lost: 18.058 (36%) Average Score: -1 Max Score: 26
#And that's what seemed to happen! Weird though! The neural nets beat the random players 58-60% of the time.
#I bet that would go down (and shift into ties) if I lowered the repeatsBeforeTie. Changed repeatsBeforeTie from 4 to 2.
#neuralVRandomEpoch([4, 5, 6, 5], 100, 1000, True, False, True, 1, 0, -1, True) #Averages: Won: 42.141 (42%) Tied: 32.49 (32%) Lost: 25.369 (25%) Average Score: 16 Max Score: 56
#And if I have them play against themselves, it evens out to about 50-50 (I remember I did this test before, but I don't think I recorded it):
#neuralVRandomEpoch([4, 5, 6, 5], 100, 1000, True, False, True, 1, 0, -1, False) #Averages: Won: 36.465 (36%) Tied: 27.989 (28%) Lost: 35.546 (36%) Average Score: 0 Max Score: 55

#neuralVRandomEpoch([4, 5, 6, 5], 10, 100, True, False, True, 1, 0, -1, True) #Averages: Won: 4.02 (40%) Tied: 3.48 (35%) Lost: 2.5 (25%) Average Score: 1 Max Score: 8
#Now switching from mnn.NeuralNet(netFormat) to rp.makeRandomNet
#neuralVRandomEpoch([4, 5, 6, 5], 10, 100, True, False, True, 1, 0, -1, True) #Averages: Won: 4.34 (43%) Tied: 3.34 (33%) Lost: 2.32 (23%) Average Score: 2 Max Score: 7
#Same results, so they are the same thing. I'm switching it back.
#This is so weird.
#I'm changing it from only being able to test a net, to just having a setupPlayerFunc that can set up any type of player
#Now I'm going to have completely random players play each other
#neuralVRandomEpoch(rp.makeRandomPlayer, 10, 100, True, False, True, 1, 0, -1, True) #Averages: Won: 3.65 (37%) Tied: 2.63 (26%) Lost: 3.72 (37%) Average Score: -1 Max Score: 6
#Almost exactly what was expected.
#neuralVRandomEpoch(rp.makeRandomPlayer, 10, 100, True, False, True, 1, 0, -1, True) #Averages: Won: 3.7 (37%) Tied: 2.68 (27%) Lost: 3.62 (36%) Average Score: 0 Max Score: 7
#Again, nothing special.
#neuralVRandomEpoch(rp.makeRandomPlayer, 10, 100, True, False, True, 1, 0, -1, False) #Averages: Won: 2.51 (25%) Tied: 3.22 (32%) Lost: 4.27 (43%) Average Score: -2 Max Score: 4
#And there's the weird one that I still can't figure out yet. Why does it lose more than it wins?