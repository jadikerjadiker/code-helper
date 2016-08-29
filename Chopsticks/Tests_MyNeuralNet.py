from MyNeuralNet import *
import random

'''            
ann = NeuralNet([4, 5, 6, 5])
ann.run([0, 0])
print(ann.activations[-1])
'''

'''
ann = NeuralNet([4, 5, 6, 5])
ann2 = NeuralNet([4, 5, 6, 5], ann.weights, ann.biases)
a = [1, 2, 3, 4]
ann.run(a)
for i in range(100):
    a[0]+=1
    print(ann.run(a)==ann2.run(a))
'''

'''
ann = NeuralNet([4, 5, 6, 5])
ann2 = ann.copy()
print(ann)
print(ann2)
ann.weights[1][0][0] = 20
print('ann')
print(ann)
print('ann2')
print(ann2)
print(ann2.weights[1].shape)
'''
'''
ann = NeuralNet([3, 5, 4, 5])
ann2 = ann.copy()
print("first ann")
print(ann)
'''
'''
print(ann.weights[1].shape)
print(ann.run([1,2, 3]))
print("shapes")
print(ann.weights[1].shape)
print(ann.weights[2].shape)
print(ann.biases[1].shape)
'''
'''
layerNum = 2
oldNpl = ann.neuronsPerLayer
ann.neuronsPerLayer[layerNum]+=1

ann.weights[layerNum] = np.append(ann.weights[layerNum], np.random.randn(1, oldNpl[layerNum-1]), axis = 0)
ann.weights[layerNum+1] = np.append(ann.weights[layerNum+1], np.zeros((oldNpl[layerNum+1], 1)), axis = 1)
ann.biases[layerNum] = np.append(ann.biases[layerNum], np.random.randn(1, 1), axis = 0)
'''
'''
ann.neuronsPerLayer = [3, 6, 4
ann.weights[1] = np.append(ann.weights[1], np.random.randn(1, 3), axis = 0)
ann.weights[2] = np.append(ann.weights[2], np.zeros((4, 1)), axis = 1)
ann.biases[1] = np.append(ann.biases[1], np.random.randn(1, 1), axis = 0)
'''
'''
print("second ann")
print(ann)
'''
'''
print('ann')
print(ann.run([1, 2, 34]))
print('ann2')
print(ann2.run([1, 2, 34]))
ann.weights[3][4][4] = 1.0
print("ann2")
print(ann2.run([1, 2, 34]))
print("ann")
print(ann.run([1, 2, 34]))
'''
'''
neuronNum = 4
ann.weights[layerNum] = np.delete(ann.weights[layerNum], neuronNum, axis = 0)
ann.weights[layerNum+1] = np.delete(ann.weights[layerNum+1], neuronNum, axis = 1)
ann.biases[layerNum] = np.delete(ann.biases[layerNum], neuronNum, axis = 0)
print("third ann")
print(ann)
print(ann2.weights==ann.weights and ann2.biases==ann.biases)
'''
'''
def changeWeight(amt):
    layerNum = random.randint(1, len(ann.neuronsPerLayer)-1) #layer that the weight will change
    layer = ann.weights[layerNum]
    layerShape = layer.shape
    #pick a random weight in the layer to change and change it
    layer[random.randint(0, layerShape[0]-1)][random.randint(0, layerShape[1]-1)] += amt

#changes a random bias by amt within the net to be mutated
def changeBias(amt):
    #choose a random layer, and then a random bias, and then change it by amt.
    layerNum = random.randint(1, len(ann.neuronsPerLayer)-1)
    layer = ann.biases[layerNum]
    ann.biases[layerNum][random.randint(0, layer.shape[0]-1)][0] = 0
    print(layer.shape[0]-1)

ann = NeuralNet([4, 3, 2, 1])
print(ann)
changeWeight(np.random.randn())
print(ann)
layer = 1
changeBias(np.random.randn())
print(ann)
'''