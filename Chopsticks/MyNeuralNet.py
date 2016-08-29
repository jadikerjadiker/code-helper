import numpy as np
import math
import copy

'''
A class that instantiates a neural net.
The net's run() function takes a list of values that will be place in its input layer and will return a numpy array of the net's output.
The weight matrix (self.weights) is a list of numpy ndarrays of shape (i, j),...
where i is the number of neurons in that layer, and j is the number of neurons in the previous layer.
The biases (self.biases) are a list of numpy ndarrays with shape (1, n), where n is the number of neurons in that layer.

We consider the input layer to actually be a layer (layer 0), but its weight matrix and bias vector are empty.
So for a NeuralNet with neuronAmts=[1, 2, 3], input layer (layer 0) will have 1 "neuron", layer 1 will have 2 neurons, and the output layer (layer 2), will have 3 neurons

The weight matrix is done so that self.weight[a][b][c] corresponds to...
the weight from the (a-1)th layer, (c)th neuron from the top/start of the list (0 would be the top neuron), to the (b)th from the top neuron in the (a)th layer
'''

class NeuralNet:
    def __init__(self, neuronAmts, weights = None, biases = None):
        '''
        print("Making a new neural net. Here's what I got for neuronAmts, weights and then biases")
        print(neuronAmts)
        print(weights)
        print(biases)
        '''
        #set up the matricies needed, putting in a blank list for the first input column of neurons.
        self.neuronsPerLayer = neuronAmts
        self.activations = [[]]*len(neuronAmts) #make neuron activation vector slots for each layer
        self.weights = weights
        self.biases = biases
        
        #setup the setup variables if they're needed
        if weights==None:
            setupWeights = [[]] #setup the random weights list with a blank space for the input layer
        else:
            self.weights = copy.deepcopy(weights)
        if biases == None:
            setupBiases = [[]] #setup the random biases list with a blank space for the input layer
        else:
            self.biases = copy.deepcopy(biases)
            
        pastv = neuronAmts[0]
        
        for i in range(1, len(neuronAmts)):
            v = neuronAmts[i]
            #use the setup variables if they're needed
            if weights==None:
                setupWeights.append(np.random.randn(v, pastv)) #creates weight matrix that can be applied to the activation vector
            if biases==None:
                setupBiases.append(np.random.randn(v, 1)) #creates bias vector for the layer
            pastv = v
            
        #set the properties to the setup variables if needed
        if weights==None:
            self.weights = setupWeights
        if biases == None:
            self.biases = setupBiases
            
        #print(self.activations)
        #print(self.weights)
        #print(self.biases)
      
    def __str__(self):
        ans = "Weights:\n"
        for i, val in enumerate(self.weights):
            ans+=str(val)+"\n"
        ans += "\nBiases:\n"
        for i, val in enumerate(self.biases):
            ans+=str(val)+"\n"
        return ans
        #return "Weights:\n{}\nBiases:\n{}".format(self.weights, self.biases)
    
    def copy(self):
        return NeuralNet(self.neuronsPerLayer, self.weights, self.biases)
    
    #takes a list of inputs and returns its answer as an np.array of its final layer.    
    def run(self, inputs):
        self.activations[0] = np.resize(np.array(inputs), (self.neuronsPerLayer[0], 1)) #set up the first activation vector to be the inputs
        for i in range(1, len(self.neuronsPerLayer)):
            self.activations[i] = self.sigmoid(np.dot(self.weights[i], self.activations[i-1])+self.biases[i])
        return self.activations[-1]
    
    #This thing causes some errors to pop up on the side of cloud9, you can just ignore them.  (This works, although I don't understand how or why at this point...)
    @np.vectorize #turns it into a function that can be applied element-wise on a column vector
    def sigmoid(num):
        return 1/(1+math.exp(num))
