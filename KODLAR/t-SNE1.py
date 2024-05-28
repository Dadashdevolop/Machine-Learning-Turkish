import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# İris veri setini yükleme
iris = load_iris()
X = iris.data

# t-SNE uygulama
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

# t-SNE sonuçlarını görselleştirme
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=iris.target)
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.title('t-SNE ile İris Veri Seti')
plt.show()


