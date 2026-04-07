
opcao = int(input("1 - Apresentação CURSO FIC\n" \
"2 - Par e Impar\n" \
"3 - Fahrenheits para Celsius e Kelvin \n" \
"4 - Numero de Caracteres" \
"\nDigite o exercicio que deseja resolver: "))

def apresentar(nome, idade, curso):
    print(f"SEJA BEM VINDOOOO!!! {nome} você tem {idade} anos!!\nVocê está no Curso FIC SENAI DE {curso}")

if opcao == 1:
    aluno = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    curso = input("Digite o seu curso: ")

    apresentar(aluno,idade,curso)

elif opcao == 2:

    def par_impar(numero):
        if numero % 2 == 0:
            print(f"O Numero {numero} é par")
        else:
            print(f"O Numero {numero} é impar")

    numero = int(input("Digite um numero: "))
    par_impar(numero)

elif opcao == 3:

    def calcular_temp(temp):

        celsius = ((temp - 32) * 5) / 9
        kelvin = ((temp - 32) / 1.8) + 273.15

        print(f"{temp} Fahrenheits em Celsius é: {celsius:.2f}")
        print(f"{temp} Fahrenheits em Kelvin é: {kelvin:.2f}")

    temp = float(input("Digite a temperatura em Fahrenheits: "))

    calcular_temp(temp)

elif opcao == 4:

    def tamanho_palavra(palavra):
        tamanho = 0
        for i in palavra:
            tamanho += 1

        print(f"O Tamanho da {palavra} é de {tamanho} de caracateres")

    palavra = input("Digite uma palavra: ")

    tamanho_palavra(palavra)
    