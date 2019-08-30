import NeuralNetwork as nn
import numpy as np

layer_sizes = (3,5,10)
x = np.ones((layer_sizes[0],1))

network = nn.NeuralNetwork(layer_sizes)
prediction = network.predict(x)

print(prediction)

# https://www.youtube.com/watch?v=8bNIkfRJZpo