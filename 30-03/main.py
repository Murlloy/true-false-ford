
while True:
        
    opcao = int(input("Digite qual exercicio quer resolver!! \n1 - Masculinos e Feminino \n2 - Numeros Pares\n3 - Media e Soma\n4 - Sistema de Cadastro\n5 - Sair\n"))

    match opcao:
        case 1:

            # definição de variaveis
            pessoas = int(input("Digite o numeros de convidados para a festa: "))
            masculinos = 0
            femininos = 0
            caminhao = 0

            for i in range(1, pessoas + 1, 1):
                
                sexo = input(f"Bem Vindo {i} Pessoa!!\nDigite o Sexo da pessoa (m) Masculino, (f) Feminino\n")
                if(sexo == "m"):
                    masculinos += 1
                    print("Masculino!!")
                elif(sexo == "f"):
                    femininos += 1
                    print("Feminino!!")
                else:
                    caminhao += 1
                    print("Desconhecido ou Caminhão!!")

            print(f"Convidados Homens: {masculinos}\nConvidados Mulheres: {femininos}\nConvidados Desconhecidos ou Caminhões: {caminhao}")

        case 2:
            # de 1 a n verificando se é par. se for ele é mostrado

            limite = int(input("Digite até onde você quer ver os numeros pares: "))

            for i in range(1, limite + 1, 1):
                if(i % 2 == 0):
                    print(i + " é par")

        case 3:

            soma = 0
            media = 0

            for i in range(1, 6, 1):
                numero = float(input("Digite um numero: "))
                soma += numero

            media = soma/5

            print(f"o valor da soma dos numeros é {soma}\nA media é {media}")

        case 4:

            print("============= Bem vindo ao criador de usuario!!! ==============\n\nTenha certeza de não por a mesma senha e mesmo usuario!!!")

            for i in range(100):
                
                user = input("\nDigite o nome de usuario: ")

                password = input("Digite uma senha: ")

                if(password == user):
                    print("\nUsuario e Senha inguais!!!!!!\n")

                else:
                    print("Sistema Acessado!!")
                    break
        case 5:
            break

    opcao = input("Deseja Sair? 1 - Sim, 2 - Não\n")
    if(opcao == "1"):
        break

