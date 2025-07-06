# inputs = [1, 2, 3, 2.5]
# weights = [[0.2, 0.8, -0.5, 1.0],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87]]
# biases = [2, 3, 0.5]

# # Output of current layer
# layer_outputs = []

# # For each neuron
# for neuron_weights, neuron_bias in zip(weights, biases):
#     # Zeroed output of given neuron
#     neuron_output = 0

#     #for each input and weight to the neuron
#     for n_input, weight in zip(inputs, neuron_weights):
#         # Multiply this input by associated weight
#         # And add to the neuron's output variable
#         neuron_output += n_input*weight

#     # Add the bias
#     neuron_output += neuron_bias
#     # Put neuron's result to the layers output list
#     layer_outputs.append(neuron_output)

# print(layer_outputs)


# 2.3 Dot product 
# import numpy as np

# inputs = [1, 2, 3, 2.5]
# weights = [[0.2, 0.8, -0.5, 1.0],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87]]
# biases = [2, 3, 0.5]

# outputs = np.dot(weights, inputs) + biases
# print(outputs)

# 2.4 Batches, layers and Objects
import numpy as np

# inputs = [[1.0, 2.0, 3.0, 2.5],
#           [2.0, 5.0, -1.0, 2.0],
#           [-1.5, 2.7, 3.3, -0.8]]

# weights = [[0.2, 0.8, -0.5, 1.0],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87]]
# biases = [2, 3, 0.5]

# weights2 = [[0.1, -0.14, 0.5],
#             [-0.5, 0.12, -0.33],
#             [-0.44, 0.73, -0.13]]
# biases2 = [-1, 2, -0.5]

# layer1_output = np.dot(inputs, np.array(weights).T) + biases
# layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2
# print(layer2_output)

np.random.seed(0)

X = [[1.0, 2.0, 3.0, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
# print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)