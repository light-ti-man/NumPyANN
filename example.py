import numpy
import nn

"""
This project creates a neural network where the architecture has input and dense layers only. More layers will be added in the future. 
The project only implements the forward pass of a neural network and no training algorithm is used.
For training a neural network using the genetic algorithm, check this project (https://github.com/ahmedfgad/NeuralGenetic) in which the genetic algorithm is used for training the network.
Feel free to leave an issue in this project (https://github.com/ahmedfgad/NumPyANN) in case something is not working properly or to ask for questions. I am also available for e-mails at ahmed.f.gad@gmail.com
"""

# Reading the data features. Check the 'extract_features.py' script for extracting the features & preparing the outputs of the dataset.
data_inputs = numpy.load("dataset_features.npy")

# Optional step for filtering the features using the standard deviation.
features_STDs = numpy.std(a=data_inputs, axis=0)
data_inputs = data_inputs[:, features_STDs > 50]

# Reading the data outputs. Check the 'extract_features.py' script for extracting the features & preparing the outputs of the dataset.
data_outputs = numpy.load("outputs.npy")

# The number of inputs (i.e. feature vector length) per sample
num_inputs = data_inputs.shape[1]
# Number of outputs per sample
num_outputs = 4

HL1_neurons = 150
HL2_neurons = 60

# Building the network architecture.
input_layer = nn.InputLayer(num_inputs)
hidden_layer1 = nn.DenseLayer(num_neurons=HL1_neurons, previous_layer=input_layer, activation_function="relu")
hidden_layer2 = nn.DenseLayer(num_neurons=HL2_neurons, previous_layer=hidden_layer1, activation_function="relu")
output_layer = nn.DenseLayer(num_neurons=num_outputs, previous_layer=hidden_layer2, activation_function="sigmoid")

# Training the network.
nn.train_network(num_epochs=10,
                  last_layer=output_layer,
                  data_inputs=data_inputs,
                  data_outputs=data_outputs,
                  learning_rate=0.01)

# Using the trained network for predictions.
predictions = nn.predict_outputs(last_layer=output_layer, data_inputs=data_inputs)

# Calculating some statistics
num_wrong = numpy.where(predictions != data_outputs)[0]
num_correct = data_outputs.size - num_wrong.size
accuracy = 100 * (num_correct/data_outputs.size)
print("Number of correct classifications :", num_correct)
print("Number of wrong classifications :", num_wrong.size)
print("Classification accuracy :", accuracy)
