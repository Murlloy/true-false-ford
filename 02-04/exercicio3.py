
while True:

    opcao = int(input("Digite qual exercicio quer resover: \n1 - 1 a 5 Numeros Inteiros\n2 - 1 a 10 de numeros Reais\n3 - Media de 4 Notas\n: "))

    if opcao == 1:
        
        numeros = []

        for i in range(5):
            
            n = int(input(f"Digite o {i + 1} valor: "))
            numeros.append(n)

        print(numeros)

    ## exercicio 2
    elif opcao == 2:

        numeros = []

        for i in range(10):
            n = float(input(f"Digite o {i + 1} valor: "))
            numeros.append(n)

        numeros.reverse()

        print(numeros)

    ## exercicio 3 

    elif opcao == 3:

        for i in range(4):

            nota = float(input(f"Digite a {i + 1} nota"))
            notas += nota

        media = notas/4

        print(f"A somas desses numeros é: {notas}")
        print(f"A media desses numeros é: {media}")

    opcao = int(input("Deseja Testar novamente?\n1 - Sim\n2 - Não\n: "))

    if(opcao == 2):
        break