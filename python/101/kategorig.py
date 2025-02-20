# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:38:55 2023

@author: Selçuk Şahin
"""

#kütüphaneler bölümü
import pandas as pd
import numpy as np
import matplotlib as plt

#veri önişleme
#2.1veri yükleme

veriler = pd.read_csv('C:/Users/Selçuk Şahin/Desktop/makine öğrenmesi/bölüm1/eksikveriler.csv')
print(veriler)

#-veri ön işleme
boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)


#eksik veriler

#sci - kit learn
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

yas = veriler.iloc[:,1:4].values
print(yas)
imputer = imputer.fit(yas[:,1:4])
yas[:,1:4] = imputer.transform(yas[:,1:4])
print(yas)

#encoder kategorik veriler => numeric
ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()



ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe = preprocessing.OneHotEncoder()

ulke = ohe.fit_transform(ulke).toarray()
print(ulke)


# numpy dizeleri dataframe dönüşümü

sonuc= pd.DataFrame(data=ulke, index= range(22), columns= ['fr','tr','us'])
print(sonuc)

sonuc2 = pd.DataFrame(data=yas , index= range(22), columns=['boy', 'kilo', 'yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3= pd.DataFrame(data=cinsiyet, index=range(22), columns=['cinsiyet'])
print(sonuc3)

#dataframe birleştime işlemi

s= pd.concat([sonuc,sonuc2], axis=1)
print(s)

s2= pd.concat([s,sonuc3], axis=1)
#print((s2))

#verilerin eğitim ve test için bölünmesi

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)

#verilerin ölçeklenmesi

from sklearn.preprocessing import StandardScaler

sc= StandardScaler()

X_train= sc.fit_transform(x_train)
X_test= sc.fit_transform(x_test)














