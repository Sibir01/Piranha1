"""
Task
Create a neural network to determine the class of an object based on two features (parameters).
We will generate random points on a plane and determine whether they belong to class 1 (if closer to the center)
or to class 0 (if further from the center).
"""

"""
Explanation of libraries:
NumPy is a library for working with multidimensional arrays and matrices, 
as well as performing various mathematical operations on them.

Keras is a high-level interface for TensorFlow that simplifies building neural networks.

Sequential is a class that is used to create a linear sequential model
(layers are added one after another). This is useful for building simple neural networks, 
where each layer sequentially follows the previous one.
Dense is a layer of a fully connected neural network, in which each neuron is connected to all neurons of the previous layer.
In this example, Dense is used to create a single fully connected layer that will be trained on our data.

Using Scikit-learn to Get Started

train_test_split — a function that splits a dataset into training and testing sets. 
This allows you to train a model on one part of the data and evaluate it on another to see if it can generalize.

accuracy_score — a function for calculating the accuracy of a model. 
It compares the model's predictions to the actual class labels,
allowing you to see how accurately the model classified the data.

pyplot is a Matplotlib module that contains functions for plotting different kinds of graphs. 
Here, plt is used to plot the model errors during training so that we can 
visually assess how the error on the training and validation data changed with each epoch.

"""



import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Generating data for the test
np.random.seed(0)
data_size = 1000
X = np.random.rand(data_size, 2) * 2 - 1  # Points on the plane within [-1, 1]
y = (np.sqrt(X[:, 0]**2 + X[:, 1]**2) < 0.5).astype(int)  # Class 1 for points closer to the center, class 0 for the rest

# We divide the data into training and test samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a test model Piranha1
model = Sequential([
    Dense(1, input_shape=(2,), activation='sigmoid')  # One neuron with sigmoid activation for testing
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model and store training history
training_history = model.fit(X_train, y_train, epochs=100, batch_size=10, validation_split=0.2)

# Predict and evaluate
y_pred = (model.predict(X_test) > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Plotting error (loss) graph
plt.plot(training_history.history['loss'], label='Training Loss')
plt.plot(training_history.history['val_loss'], label='Validation Loss')
plt.title('Error graph')
plt.xlabel('Epochs')
plt.ylabel('Error')
plt.legend()
plt.show()

"""
Data Generation: 
We create 1000 random points on the plane and assign class 1 to those closest to the center 
(within a radius of 0.5), while the rest of the points are assigned class 0.

Model Creation:

We use a single layer with a single neuron to build a simple model that mimics logistic regression. 
The sigmoid activation makes the neuron's output a number between 0 and 1, allowing it to be interpreted as a probability.
Compilation and Training:

The loss function is binary_crossentropy, which is suitable for binary classification problems. 
The adam optimizer ensures efficient training.
We train the model for 100 epochs, which gives it time to "learn" how to distinguish classes based on our data.
Evaluation and Prediction:

The model predicts the class probability for each object in the test set, and we interpret the result as "1" if 
the probability is greater than 0.5, and "0" otherwise.
Using accuracy_score, we measure the accuracy of the model on the test data.
Visualizing the error:

We plot the error on the training and validation sets by epoch to see how the model has been trained. 
If the error on the validation increases, this may indicate overfitting.



CONCLUSION:
1.The idea of initially declaring the categories to which an object may belong when setting up its AI is worth refining, 
since in the end I want the AI to create the categories itself.
2.I need a three-dimensional space, not a plane (Not a fact, but I need to check)

"""


