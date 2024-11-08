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

# Piranha1
Neural network test based on Tree

Using a Decision Tree to Get the Results You Want

Instead of dividing the classes linearly, as logistic regression did,
a decision tree will sequentially split the data into groups to minimize error.
The basic idea is to ask questions about the data
(e.g., "Is X1 greater than 0.5?") and build a structure that makes choices at each step, getting closer to the final class.

I use DecisionTreeClassifier from the sklearn library.
The max_depth parameter limits the depth of the tree, which helps prevent overfitting (requires further study).

The model predicts classes for the test set, and we evaluate its accuracy using the accuracy_score function.

The larger the max_depth, the more detailed the tree can subdivide the space.

Was able to achieve 96.33% accuracy by changing max_depth to 5.

RESULT: SUITABLE
