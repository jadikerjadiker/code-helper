import numpy as np
import MyNeuralNet as mnn

class RandomPlayer():
    def run(self, *fakeArgs):
        return np.random.randn(5, 1)
    
def makeRandomNet(form = [4, 5, 6, 5]):
    return mnn.NeuralNet(form)
    
def makeRandomPlayer():
    return RandomPlayer()