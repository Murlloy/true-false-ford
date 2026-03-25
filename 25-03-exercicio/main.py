
soma = 0
qt_notas = 0

opcao = int(input("1 - Exercicio 1" \
"\n2 - Exercicio 2"\
"\n3 - Exercicio 3"\
"\n4 - Exercicio 4"\
"\n5 - Exercicio 5"\
"\n6 - Exercicio 6 \n7 - Fibonacci"))

if(opcao == 1):
    while True:
        try:
            numero = float(input("Digite um numero entre 1 e 10\n"))
            if(numero > 10 or numero < 0):
                print("Valor invalido")
            else:
                print(f"Valor escolhido {numero}")
                break
        except ValueError:
            print("Tente um numero")

elif(opcao == 2):

    while True:

        nota = float(input(f"Digite a {qt_notas}o Nota: "))
        soma += nota 
        desejo = input("Deseja Sair? 1 - Sim, 2 - Não\n")
        if(desejo == "sim" or desejo == "s"):
            media = soma/qt_notas
            print(f"Total de notas colocadas {qt_notas}")
            print(f"Média: {media}")
            break
        qt_notas += 1

elif(opcao == 3):

    qt_turmas = input("Digite a quantidade de turmas: ")
    turma_atual = 1

    while turma_atual <= qt_turmas:
        print(f"Turma {turma_atual}")
        nome_turma = input("Digite o nome da turma: ")
        alunos = input("Digite a quantidade de alunos na turma: ")

elif(opcao == 7):

    numero_inicial = 0
    numero_atual = 1
    numero_proximo = numero_atual + numero_inicial

    print(numero_inicial)

    while True:
        numero_inicial = numero_atual
        numero_atual = numero_proximo
        numero_proximo = numero_proximo + numero_atual

        print(numero_inicial)
        print(numero_atual)
        print(numero_proximo)

        if(numero_proximo >= 500):
            break

