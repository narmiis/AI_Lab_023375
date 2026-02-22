import numpy as np

# AND gate data
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0,0,0,1])

# Initialize weights and bias
w = np.zeros(2)
b = 0
lr = 0.1

# Activation function
def step(z):
    return 1 if z >= 0 else 0

# Training
for epoch in range(10):
    for i in range(len(X)):
        z = np.dot(w, X[i]) + b
        y_pred = step(z)
        error = y[i] - y_pred
        w += lr * error * X[i]
        b += lr * error

print("Weights:", w)
print("Bias:", b)
