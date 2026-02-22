import numpy as np

X = np.array([[0], [1]])
y = np.array([1, 0])

w = np.zeros(1)
b = 0
lr = 0.1

def step(z):
    return 1 if z >= 0 else 0

for epoch in range(10):
    for i in range(len(X)):
        z = np.dot(w, X[i]) + b
        y_pred = step(z)
        error = y[i] - y_pred
        w += lr * error * X[i]
        b += lr * error

print("Weight:", w)
print("Bias:", b)
