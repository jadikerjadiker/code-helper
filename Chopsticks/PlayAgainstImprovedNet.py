import MakeRandomImprovements as mri
import VerboseGames as vg

winners = mri.makeRandomImprovements(neuralTopology = [4, 5, 6, 5], poolSize = 100, lossGoalPc = 0, winGoalPc = .4, goalGamesToPlay = 200, gamesPerRound = 99, scoring = [1, 0, -100],
                            keep = 20, mutateFactor = 5, mutationAmtPcs = 98*[1] + 2*[2]+ 2*[3] + 2*[4] + 1*[5], changeTopologyPc = .01, addNeuronsPc = .7, changeWeightPc = .6,
                            neuronAmtPcs = [1], weightBiasChangeMagnitudePcs = 49*[.1] + 1*[.5], weightBiasAmtPcs = 89*[1]+10*[2]+1*[3])

print("Here are the winners:")
for i, winner in enumerate(winners):
    print(winner)
    
print("Now, we'll have you play against the top net. Good luck!")
vg.humanVComputerGame(winners[0].copy)