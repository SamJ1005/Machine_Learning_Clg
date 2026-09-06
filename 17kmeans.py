import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data
data = pd.read_csv("kmeans.csv")

# Select features
X = data[["StudyHours", "Marks"]]

# Create K-Means model
model = KMeans(n_clusters=2, random_state=0, n_init=10)
model.fit(X)

# Display results
print("Cluster Labels:", model.labels_)
print("Cluster Centers:")
print(model.cluster_centers_)

# Plot clusters
plt.scatter(X["StudyHours"], X["Marks"], c=model.labels_)
plt.scatter(model.cluster_centers_[:, 0],
            model.cluster_centers_[:, 1],
            marker="X", s=200)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("K-Means Clustering")
plt.show()