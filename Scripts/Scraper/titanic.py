# -*- coding: utf-8 -*-
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas


df = pandas.read_csv('https://storage.googleapis.com/kaggle-competitions-data/kaggle/3136/train.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1556586075&Signature=K34j2B%2BIrbTgPeoyNjy11dSFB%2Fq5%2BeavG%2FP1%2F%2FQyQ9w7fKw0HrdHetb3FGvwScttjZy01Bndpbh%2FuXIoAyeYUBcaWFG3CS%2F8Cp%2B1z28DTiZ6BIggjkdyghFUGw6209h4tCMattM1BwzT19QdNkK18KguiRJ84rGXGXE2%2BChXftMDXjIIypst3zw9Fv3xINdqIYGmO4ZS5wacIKL8%2BTZler%2B%2BYEwAaRGE0AgO11h%2Fd597XPLiyHunEcvcoNKVGnDk7zUxKe%2B5LZ053XdNx0idMPunwfQy7O7oBm93w8TpXm1pEiCpZk3rkeCRAYpFBr2JStlO31hbCY%2FbTO5ua4sGYA%3D%3D').set_index('PassengerId')

df_formatted = df.reindex(['Pclass', 'Sex', 'Age', 'SibSp',  'Parch',  'Fare', 'Survived'], axis=1)

df_formatted['Fare'] = df_formatted['Fare'] / df_formatted['Fare'].max()

proportion = 0.2
train = pandas.DataFrame()
test = pandas.DataFrame()

train, test = train_test_split(df_formatted, test_size=proportion)

train_x = train.iloc[:, :-1]
train_y = train.iloc[:, -1]

rForest = RandomForestClassifier(n_estimators=100)

pass