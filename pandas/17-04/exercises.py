import pandas as pd

# carregar sua tabela (exemplo: CSV)
df = pd.read_excel("pandas/17-04/vinhos_exercicio.xlsx")

# média da população
media_pop = df["volume_hl"].mean()

medias_amostras = []

for i in range(5):
    amostra = df.sample(frac=0.05, replace=False, random_state=i)
    media = amostra["volume_hl"].mean()
    medias_amostras.append(media)
    print(f"Amostra {i+1} - média: {media:.4f}")

print(f"\nMédia da população: {media_pop:.4f}")


print("\n\n================= EXERCICIO 2 ================\n\n")

_ = input("\n -- Digite qualquer coisa para passar --")


for i, m in enumerate(medias_amostras):
    diferenca = m - media_pop
    print(f"Amostra {i+1}: média = {m:.4f} | diferença para população = {diferenca:.4f}")



print("\n\n================= EXERCICIO 3 ================\n\n")

_ = input("\n -- Digite qualquer coisa para passar --")