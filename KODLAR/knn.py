import pandas as pd
import numpy as np
from warnings import filterwarnings
filterwarnings('ignore')
df = pd.read_csv('veriler.csv')
df.head()
df=df.rename(columns={"X1 transaction date":"İşlem Tarihi",
                  "X2 house age":"Ev Yaşı",
                  "X3 distance to the nearest MRT station":"Metroya Olan Uzaklık",
                  "X4 number of convenience stores":"Civardaki Market Sayısı",
                  "X5 latitude":"Enlem",
                  "X6 longitude":"Boylam",
                  "Y house price of unit area":"Birim Alan Fiyatı"})
df.head()
x=df.drop(columns="Birim Alan Fiyatı")#bağımsız değişken
y=df["Birim Alan Fiyatı"]#bağıml
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split,GridSearchCV
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=42)
knn_model=KNeighborsRegressor()
knn_model.fit(x_train,y_train)
knn_model.n_neighbors
knn_model.metric
knn_params={"n_neighbors":np.arange(1,100,1)}
knn_cv_model=GridSearchCV(knn_model,knn_params,cv=10).fit(x_train,y_train)
knn_cv_model.best_params_
knn_tuned=KNeighborsRegressor(n_neighbors=knn_cv_model.best_params_["n_neighbors"]).fit(x_train,y_train)
y_pred=knn_tuned.predict(x_test)#tahmin
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
print("KNN Modeli Hata Kareler Ortalaması",mse)
