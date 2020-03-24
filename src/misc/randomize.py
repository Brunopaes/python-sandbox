import pandas
import random


df = pandas.read_csv('https://raw.githubusercontent.com/Brunopaes/picpay-sherock_holmes/master/data/datasource.csv')
df_fraud = df[df['Fraude'] == 1]
df_non = df[~df.index.isin(df_fraud.index)]

k = list(df_fraud.columns)
v = []
for i in df_fraud.columns[:-1]:
    max_ = df_fraud[i].max()
    min_ = df_fraud[i].min()

    v.append([random.uniform(min_, max_) for i in range(len(df_non))])

df_gan = pandas.DataFrame(dict(zip(k, v)))
df_gan['Fraude'] = 1

df_final = df_non.append(df_gan).reset_index(drop=True)

df_final.to_csv('new_train.csv')
df_fraud.to_csv('validation.csv')
