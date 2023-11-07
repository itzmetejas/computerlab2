import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import linkage,dendrogram

data = pd.read_csv('churn.csv')
data

X = data[['Age','Tenure','Balance','CreditScore','EstimatedSalary']]
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X)

agg_cluster = AgglomerativeClustering(n_clusters = 3)
agg_labels = agg_cluster.fit_predict(X_Scaled)

linked = linkage(X_Scaled,'ward')
dendrogram(linked,orientation='top',distance_sort='descending',show_leaf_counts='True')
plt.show()

plt.scatter(X_Scaled[:,0],X_Scaled[:,1],c=agg_labels,cmap='rainbow')
plt.show()
