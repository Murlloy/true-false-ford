#Exercise 1

import pandas as pd
import numpy as np

df = pd.read_csv("pandas/vinhos.csv")

print(df.head(5))
print(df.shape)
print(df.dtypes)
print(df.describe())

#Exercise 2

print(df.describe().T)

#Exercise 3

df_copy = df.copy()

for _ in range(20):
    i = np.random.randint(0, df_copy.shape[0])
    j = np.random.randint(0, df_copy.shape[1])
    df_copy.iat[i,j] = np.nan

print("\nQuantidade de valores nulos por coluna:")
print(df_copy.isnull().sum())

print("\nDescribe original (transposto):")
print(df.describe().T)

print("\nDescribe com valores nulos (transposto):")
print(df_copy.describe().T)