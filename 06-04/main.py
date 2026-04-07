
opcao = int(input("1 - 4 Tupla de Numeros Inteiros\n" \
"2 - Duas Tuplas\n" \
"3 - Conversão de Tupla \n" \
"\nDigite o exercicio que deseja resolver: "))

if opcao == 1:
    tupla = (1,2,3,4)
    print(tupla[1])

elif opcao == 2:
    tupla_numero = (10,20,40,50,30)
    tupla_palavras = ("Arroz", "Peixe", "Pão", "Macarrão")

    print(tupla_numero[2])
    print(tupla_palavras[3])

elif opcao == 3:
    tupla = (5,10,15,20)

    tupla_lista = list(tupla)
    tupla_lista.append(25)
    tupla = tuple(tupla_lista)

    print(tupla)