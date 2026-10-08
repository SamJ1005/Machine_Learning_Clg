import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering

data=pd.read_csv("agg.csv")

dist_matrix = squareform(pdist(data, metric="euclidean"))
print("Distance Matrix:\n", pd.DataFrame(dist_matrix, index= data.index, columns=data.index),"\n")

agg=AgglomerativeClustering(n_clusters=2, linkage="single")
labels=agg.fit_predict(data)

data["Cluster"]=labels
print("Data with assigned clusters:\n", data)

Z=linkage(pdist(data[["x1","x2"]]), method="single")

plt.figure()
dendrogram(Z, labels=[f"p{i}" for i in data.index])
plt.title("Dendrogram (Single Linkage)")
plt.xlabel("Data points")
plt.ylabel("Distance")
plt.show()