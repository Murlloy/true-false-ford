
qt_convidados = int(input("Digite a quantidade de convidados para sua festinha:\n"))
pessoas = 1

pessoas_barradas = 0

while pessoas <= qt_convidados:
    idade_pessoa = int(input(f"Bem vindo {pessoas} pessoa!\nQual a sua idade:"))
    if(idade_pessoa >= 18):
        print("Pode entrar")
    else:
        convite = input("Você possui o convite? sim ou não")
        if(convite == "sim"):
            convite = True
        else:
            convite = False
        if(convite == True):
            print("Você passou!")
        else:
            print("Você foi barrado pela segurança!")
            pessoas_barradas += 1

    pessoas += 1
    

print(f"pessoas barradas {pessoas_barradas}")
    
