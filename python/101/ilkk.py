# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:38:55 2023

@author: Selçuk Şahin
"""

#kütüphaneler bölümü
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#kodlar
#-veri yükleme

veriler = pd.read_csv('C:/Users/Selçuk Şahin/Desktop/makine öğrenmesi/bölüm1/eksikveriler.csv')
print(veriler)

#-veri ön işleme
boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)


class insan:
    boy = 180
    def kosmak(self,b):
        return b+10
ali = insan()        
print(ali.boy)
print(ali.kosmak(90))

#eksik veriler

#sci - kit learn
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

yas = veriler.iloc[:,1:4].values
print(yas)
imputer = imputer.fit(yas[:,1:4])
yas[:,1:4] = imputer.transform(yas[:,1:4])
print(yas)














