
qt_convidados = int(input("Digite a quantidade de convidados para sua festinha:\n"))
pessoas = 1

pessoas_barradas = 0
sem_convites = 0
entradas = 0

while pessoas <= qt_convidados:
    idade_pessoa = int(input(f"Bem vindo {pessoas} pessoa!\nQual a sua idade: "))

    convite = input("Você possui o convite? sim ou não\n")
    if(convite == "sim"):
        convite = True
        entradas += 1
    else:
        if(idade_pessoa>= 18):
            convite = True
            entradas += 1
            sem_convites += 1
        else:
            convite = False
    if(convite == True):
        print("\nVocê passou!\n")
    else:
        print("\nVocê foi barrado pela segurança!\n")
        pessoas_barradas += 1

    pessoas += 1
    

print(f"pessoas barradas: {pessoas_barradas}")
print(f"pessoas que entraram: {entradas}")
print(f"pessoas que entraram sem convite: {sem_convites}")
