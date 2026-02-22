from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

data = load_iris()
X = data.data

model = KMeans(n_clusters=3)
model.fit(X)

print("Cluster Centers:\n", model.cluster_centers_)
