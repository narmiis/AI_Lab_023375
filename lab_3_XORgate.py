from sklearn.neural_network import MLPClassifier
import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0,1,1,0])

model = MLPClassifier(hidden_layer_sizes=(2,), max_iter=1000)
model.fit(X,y)

print("Predictions:", model.predict(X))
