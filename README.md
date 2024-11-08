# Piranha1
Neural network test based on linear regression

check if the principles of linear regression are suitable for the "ADAM" project

1. Generating data
Generate 1000 random points on the plane ranging from -1 to 1 in both coordinates.
Assign class 1 to points that are closer to the center (within a radius of 0.5), and class 0 to those that are further from the center. This way, the dataset simulates a circle, where points inside the circle belong to one class, and outside the circle to another.
2. Creating a neural network
I built a model with one fully connected layer (Dense) and one neuron with sigmoid activation. This is a simplified model for binary classification, similar to logistic regression.
The sigmoid activation function allows you to output the result as a probability of belonging to one of the classes.
3. Compiling the model
We use the binary_crossentropy loss function, which is suitable for binary classification problems.
The adam optimizer helps to efficiently tune the weights in the model.
4. Model training
The model was trained on 100 epochs with mini-samples of 10 points.
Allocating 20% ​​of the data for validation (validation_split=0.2) allows you to monitor errors on the holdout sample and observe possible overfitting.
5. Model evaluation
After training, the model was tested on test data that it had not seen before. You obtained the model's predictions and calculated the accuracy to see how well the model classifies the data.

RESULT: NOT SUITABLE
