

while True:
    n1 = float(input("Digite a primeira nota: "))
    if(n1 > 10 or n1 < 0):
        print("\n Valor Incorreto !!!\n")
    else:
        break

while True:
    n2 = float(input("Digite a segunda nota: "))
    if(n2 > 10 or n2 < 0):
        print("\n Valor Incorreto !!!\n")
    else:
        break

while True:
    n3 = float(input("Digite a terceira nota: "))
    if(n3 > 10 or n3 < 0):
        print("\n Valor Incorreto !!!\n")
    else:
        break

media = (n1 + n2 + n3) / 3

if(media >= 7):
    print("\n======= Você Passou !! =======")
elif(media >= 5):
    print("\n======= Recuperação !! =======")
else:
    print("\n======= REPROVOU  !!  =======")

print(f"\nSua média: {media:.2f}\n")