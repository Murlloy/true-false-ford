
import pandas as pd

import numpy as np

df = pd.read_excel("vinhos_exercicio.xlsx")

# print(df[df['grape_type'] == "Wine"])
# print(df[df['location_type'] == "Brazil_State"])
# print(df[df['category'] == "Sales"])

df_copy = df.copy()

#Busca por condições ==
# data_frame[ AQUI VEM A BUSCA ]
# cachorros tipo vira-lata
# df_dogs[df_dogs['type_dog'] == 'Vira Lata']
#

#  BUSCA POR VARIAS CONDIÇÕES

# df_dogs[(df_dogs[CONDICIONAL 1]) & (df_dogs[CONDICIONAL 2])]

first_df = df_copy[(df_copy['grape_type'] == "Wine") & (df_copy['category'] == "Sales") & (df_copy['location_type'] == "Brazil_State")]
print(first_df)

df_copy = df.copy()

second_df = df_copy[(df_copy['grape_type'] == 'Table') & (df_copy['category'] == 'Sales')]
print(second_df)

print(first_df.describe().T)
print(second_df.describe().T)

mean_first = first_df['value_usd'].mean()
mean_second = second_df['value_usd'].mean()

print("Média first_df:", mean_first)
print("Média second_df:", mean_second)

if mean_first > mean_second:
    print("o primeiro banco tem a maior média")
else:
    print("o segundo banco tem a maior média")

print("\n\n================= EXERCICIO 2 ================\n\n")

_ = input("\n -- Digite qualquer coisa para passar --")

print("Primeiro Banco ============ \nOrdenado Decrescente!!")

print(first_df.sort_values(by='year', ascending=False))
print(first_df.sort_values(by='value_usd', ascending=True))

print(first_df.iloc[:, [0,1,4,5,6]])

print("\n\n================= EXERCICIO 3 ================\n\n")

_ = input("\n -- Digite qualquer coisa para passar --")

print(first_df.loc[first_df.index[:10]])
print(second_df.loc[second_df.index[:10]])

print("\n\n================= EXERCICIO 4 ================\n\n")

_ = input("\n -- Digite qualquer coisa para passar --")

# Primeiro Exercicio 

# Qual UF, possuí maior  “value_usd” para vinhos do tipo Wine na categoria “Sales”? Use o sort_by e o head(1) para mostrar o resultado.

print("========= PRIMEIRA PERGUNTA ==========")

wine_sales = df[(df['grape_type'] == 'Wine') & (df['category'] == 'Sales')]

top_uf = wine_sales.sort_values(by='value_usd', ascending=False).head(1)

print(top_uf)

# EXERCICIO 2   Olhando para a base toda qual location possuí maior valor de importação? Use o sort_by e o head(1) para mostrar o resultado.

print("========= SEGUNDA PERGUNTA ==========")

imports = df[df['category'] == 'Import']

top_import = imports.sort_values(by='value_usd', ascending=False).head(1)

print(top_import)

# QUESTÃO 3  Olhando para a base toda qual location possuí maior valor de exportação? Use o sort_by e o head(1) para mostrar o resultado.

print("========= TERCEIRA PERGUNTA ==========")

exports = df[df['category'] == 'Export']

top_export = exports.sort_values(by='value_usd', ascending=False).head(1)

print(top_export)

