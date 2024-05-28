import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Verilerin yüklenmesi
musteriler = pd.read_csv('musteriler.csv')

# Bağımsız değişkenlerin seçilmesi
X = musteriler.iloc[:, 3:].values

# K-Means kümeleme modelinin oluşturulması ve eğitilmesi
from sklearn.cluster import KMeans

kume_sayisi = 3
kmeans = KMeans(n_clusters=kume_sayisi, init='k-means++')
kmeans.fit(X)

# Küme merkezlerinin görüntülenmesi ve yorumlanması
print("Küme Merkezleri:")
print(kmeans.cluster_centers_)
print("\nBu küme merkezleri, her bir kümeye ait merkez noktalarını temsil eder.")
print("Her bir kümenin merkezi, o kümenin karakteristik özelliklerini yansıtır.")

# Elbow yöntemi ile optimum küme sayısının belirlenmesi
inertias = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=123)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# Elbow metodu grafiği
plt.plot(range(1, 11), inertias)
plt.title('Elbow Yöntemi ile Optimum Küme Sayısı Belirleme')
plt.xlabel('Küme Sayısı')
plt.ylabel('İç İçe Geçmiş Kareler Toplamı (Inertia)')
plt.show()
