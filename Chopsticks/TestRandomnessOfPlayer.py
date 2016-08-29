import NeuralToChopsticks as ntc
import ChopsticksGame as cg
import RandomPlayers as rp
import numpy as np
import random

def makeRandomGame():
    return [[random.randint(0, 4), random.randint(0, 4)], [random.randint(0, 4), random.randint(0, 4)]]

def test(setupPlayerFunc, movesToMake, realSituation = False):
    moves = [0]*5 #five slots, one for each move
    c = cg.ChopsticksGame(trackTies = False)
    h = ntc.NeuralToChopsticks(c)
    for i in range(movesToMake):
        c.game = makeRandomGame()
        #print(c.gameOver())
        while not isinstance(c.gameOver(), bool) or c.gameOver():
            c.game = makeRandomGame()
            #print(c.gameOver())
            #print(c)
            
        #print(c)
        player = setupPlayerFunc()
        #print("About to make move")
        if realSituation: #record the move possible for the game that the player would make
            move = h.haveNetMakeMove(player)-1
        else: #just see what move the net would make
            possMoves = np.ndarray.tolist(player.run(h.convertGameToNet()))
            move = possMoves.index(max(possMoves))
        #print("Move: {}".format(move))
        moves[move]+=1
        #print("Moves updated.")
        print("{}%...".format(round(100.0*(i+1)/movesToMake, 1)))
    
    percents = [int(round(100.0*num/movesToMake)) for num in moves]
    
    print("1: {} {}%    2: {} {}%    3: {} {}%    4: {} {}%    5: {} {}%    ".format(moves[0], percents[0], moves[1], percents[1], moves[2], percents[2], moves[3], percents[3], moves[4], percents[4]))
    
#test(rp.makeRandomNet, 100000)
#Got 20% for all on both rp.makeRandomNet and rp.makeRandomPlayer
#Now I'm going to record what the results are for actual game positions:
#test(rp.makeRandomPlayer, 100000, True) #1: 23327 23%    2: 23447 23%    3: 23344 23%    4: 23433 23%    5: 6449 6%
#test(rp.makeRandomNet, 100000, True) #1: 23526 24%    2: 23008 23%    3: 23453 23%    4: 23392 23%    5: 6621 7%    
#So there's a very, very slight difference. Not enough to cause a ten percent difference in games though.

import MyNeuralNet as mnn
net = mnn.NeuralNet([4, 5, 6],
weights = 
[[],
[[-0.97483412, -0.02435693,  0.48447167, -0.10641175],
 [ 0.31797426,  0.02961035,  1.0606121,  -0.5762177 ],
 [ 0.67133147,  1.40375944,  2.00689994, -0.23306224],
 [-0.99862622, -1.35436044, -1.35255715, -0.32429789],
 [ 1.27501455, -0.64065041, -1.29292916, -1.70974644]],
[[ 1.31379805, -1.03055192,  1.06469668,  0.31770251,  1.04343256],
 [-1.33340669,  0.44470308,  1.49226326,  0.75347302, -0.57826412],
 [-0.31312335,  0.21682511,  0.02365975,  0.54726041,  0.34537645],
 [ 0.46888856,  2.01029208,  0.62644518, -0.22338053,  0.40043938],
 [ 0.3075504,   1.69249138, -1.21421438,  0.97047855, -0.75535553],
 [-0.10595831,  0.20447939,  0.68989505, -0.53556624,  0.95752735]],
[[-0.37934154,  0.50758469, -0.61910639,  0.08022022, -0.92984066,  0.2047193 ],
 [-1.63162403,  0.05676542,  1.31551776, -0.55843083, -0.11505383,  0.35081389],
 [ 2.26670532,  0.31578952,  0.97738802, -2.4780149,  -0.42786842, -1.64187693],
 [ 0.41953581,  1.03166673,  1.66941635,  1.5243786,  -0.19635009, -1.36925707],
 [-0.85683744, -1.42569012, -0.35529888, -0.44927638, -0.72990177, -0.61110682]]],
biases = 
[[],
[[ 1.79266702],
 [-0.45855466],
 [ 0.17360462],
 [-1.23387701],
 [ 0.13526479]],
[[ 0.02764461],
 [-1.30990301],
 [-0.27175546],
 [-2.23523803],
 [ 0.60545063],
 [-0.1048743 ]],
[[-1.90491696],
 [ 1.27084833],
 [-0.21066639],
 [-0.73081205],
 [-1.72502278]]])
 
test(net.copy, 10000, True)
