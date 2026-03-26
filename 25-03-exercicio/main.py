
soma = 0
qt_notas = 1

opcao = int(input("============= BEM VINDO AO RESOLVEDOR DE EXERCICIOS FORD ===============\n\n1 - Exercicio 1" \
"\n2 - Exercicio 2"\
"\n3 - Exercicio 3"\
"\n4 - Exercicio 4"\
"\n5 - Exercicio 5"\
"\n6 - Exercicio 6 \n7 - Fibonacci\n8 - Sair\n\nDigite oque quer fazer: "))

if(opcao == 1):
    while True:
        try:
            numero = float(input("\n========== DE 1 A 10 ==========\nDigite um numero entre 1 e 10\n:"))
            if(numero > 10 or numero <= 0):
                print("Valor invalido")
            else:
                print(f"=== Valor escolhido {numero} ===")
                break
        except ValueError:
            print("Tente um numero")

elif(opcao == 2):

    while True:

        
        nota = float(input(f"\n============ MEDIA =============\nDigite a {qt_notas}o Nota: "))
        soma += nota 
        desejo = input("Deseja Sair? 1 - Sim, 2 - Não\n").lower
        if(desejo == "sim" or desejo == "s" or desejo == "1"):
            media = soma/qt_notas
            print(f"Total de notas colocadas {qt_notas}")
            print(f"====== Média: {media} ======")
            break
        qt_notas += 1

elif(opcao == 3):

    print("\n=========== SISTEMA DE CONTAR TURMAS =============\n")

    while True:
        qt_turmas = int(input("Digite a quantidade de turmas: "))
        if(qt_turmas > 0 and qt_turmas <= 10):
            break
        else:
            print("O maximo turmas atualmente são 10 turmas!!")
    turma_atual = 1
    total_alunos = 0
    max_alunos = 0
    max_turma = ""

    while turma_atual <= qt_turmas:
        print(f"Turma {turma_atual}")
        nome_turma = input("Digite o nome da turma: ")
        while True:
            alunos = int(input("Digite a quantidade de alunos na turma: "))
            if(alunos > 40):
                print("Invalido")
                print("Quantidade superior a 20 alunos!")
            elif(alunos <= 0):
                print("\nInvalido")
                print("Valor invalido de alunos\n")
            else:
                break
        
        if(alunos > max_alunos):
            max_alunos = alunos
            max_turma = nome_turma

        total_alunos += alunos
        turma_atual += 1

    media = total_alunos/qt_turmas

    print(f"\n=== Turma com mais alunos: {max_turma} ===")
    print(f"Quantidade da maior turma: {max_alunos}\n=================================\n")

    print(f"Total de Turmas: {qt_turmas}")
    print(f"Total de Alunos: {total_alunos}")
    print(f"=== Média de Alunos: {media} ===")

elif(opcao == 4):

    print("\n============ CASAS DECIMAIS =============")

    numero = int(input("Digite um valor e vamos descobrir quantas casa decimais ele tem!\n"))
    qt_vezes = 0

    while numero >= 1:
        numero/= 10
        qt_vezes += 1

    print(f"\n========= Esse numero contem {qt_vezes} casas decimais ==========")

elif(opcao == 5):

    print("============== VERIFICADOR DE SENHA 1200 ============")

    senha = input('Crie uma senha: ')
    entrada_senha = input("Digite novamente sua senha: ")
    
    while entrada_senha != senha:
        print("\nInvalido!\n")
        entrada_senha = input("Digite novamente sua senha: ") 

    print("\nSucesso :D \n========== Senha Cadastrada! ==========")

elif opcao == 6:

    print("\n================= BEM VINDO AO SOMADOR 2000 ================\n")
    numero = int(input("Digite um numero: " ))

    soma = numero
    qt_numeros = 1

    while numero != 0:
        numero = int(input("Digite um numero: " ))
        soma += numero
        qt_numeros += 1

    media = soma/qt_numeros

    print(f"A Soma de todos esses numeros é {soma}")
    print(f"A Media desses {qt_numeros} numeros é {media}")

elif opcao == 7:

    max_fabonacci = int(input("\n================== TRIPONACCI =================\nAté que numero gostaria que o TRIPONACCI fosse?\n"))

    inicial_1 = 0
    inicial_2 = 1

    proximo = inicial_1 + inicial_2

    print(inicial_1)
    print(inicial_2)
    print(proximo)

    while proximo < max_fabonacci:
        inicial_1 = inicial_2
        inicial_2 = proximo
        proximo = inicial_1 + inicial_2

        if(proximo > max_fabonacci):
            break

        print(proximo)

elif opcao == 8:
    
    max_tribonacci = int(input("\n================== TRIPONACCI =================\nAté que numero gostaria que o TRIPONACCI fosse?\n"))

    inicial_1 = 0
    inicial_2 = 1
    inicial_3 = 1

    proximo = inicial_1 + inicial_2 + inicial_3

    print(inicial_1)
    print(inicial_2)
    print(inicial_3)
    print(proximo)

    while proximo < max_tribonacci:
        inicial_1 = inicial_2
        inicial_2 = inicial_3
        inicial_3 = proximo
        proximo = inicial_1 + inicial_2 + inicial_3

        if(proximo > max_tribonacci):
            break

        print(proximo)

