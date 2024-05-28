import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# İris veri setini yükleme
iris = load_iris()
X = iris.data

# PCA uygulama
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# PCA sonuçlarını görselleştirme
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA ile İris Veri Seti')
plt.show()

