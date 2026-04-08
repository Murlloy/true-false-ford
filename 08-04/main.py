
opcao = int(input("1 - Contar Pares\n" \
"2 - Ao Cubo de numeros\n" \
"3 - Lista de Compras \n" \
"4 - Divisão segura\n" \
"5 - Dicionario de produtos com Preços"
"\nDigite o exercicio que deseja resolver: "))

if opcao == 1:

    numeros = []

    def contar_par(*args):

        par = 0
        impar = 0

        for i in args:
            if(i % 2 == 0):
                par+=1
            else:
                impar+= 1

        print(f"Nessa Lista de numeros contem {par} pares e {impar} impares")

    contar_par(4,4,5,6,1,2,4,5)

elif opcao == 2:

    def cubica(*nums):

        numeros = []

        for num in nums:
            print(f"O Cubico de {num} é: {num * num * num}")
            numeros.append(num)
    
    cubica(4,3,7,8,6,3)

elif opcao == 3:

    lista_compras = [

        {
            "nome": "PlayStation 4",
            "preco": 2500
        },
        {
            "nome": "Controle de PS5",
            "preco": 600
        },
        {
            "nome": "Red Dead Redemption 2",
            "preco": 150
        },
    ]

    def calcular_total(lista):

        total = 0

        for l in lista:
            total += l["preco"]
            print(f"Produto: {l["nome"]} ======== Preço: R${l["preco"]},00")

        print(f"Total: R${total},00")

    print("=========== Carrinho De Compras =========")
    calcular_total(lista_compras)

elif opcao == 4:

    def divisao_segura(): 
        try:
            num1 = float(input("Digite o primeiro valor: "))
            div = float(input("Digite o valor que deseja dividir ele: "))

            resultado = num1 / div

            print(f"O Resultado da divisão é: {resultado}")

        except ZeroDivisionError:
            print("Impossivel!! Dividir por zero!")

        finally:
            print("Finalizando...")

    divisao_segura()

elif opcao == 5:

    produtos = {
            1: {
                "nome_produto": "Lontra Domestica",
                "preco": 200
            },
            2: {
                "nome_produto": "Capivara Relaxada",
                "preco": 150
            },
            3: {
                "nome_produto": "Pato de Botas",
                "preco": 120
            },
            4: {
                "nome_produto": "Gato Ninja",
                "preco": 180
            },
            5: {
                "nome_produto": "Cachorro Astronauta",
                "preco": 250
            },
            6: {
                "nome_produto": "Coelho Mágico",
                "preco": 130
            },
            7: {
                "nome_produto": "Raposa Hacker",
                "preco": 300
            },
            8: {
                "nome_produto": "Urso Gamer",
                "preco": 220
            },
            9: {
                "nome_produto": "Tartaruga Zen",
                "preco": 140
            },
            10: {
                "nome_produto": "Coruja Sábia",
                "preco": 160
            },
            11: {
                "nome_produto": "Leão Rei",
                "preco": 350
            }}

    def buscar_preco_por_id(id):
        try:
            produto = produtos[id]
            print(f"===== {produto['nome_produto']} =====")
            print(f"O preço desse produto é: R${produto['preco']}")
        except KeyError:
            print("Valor inválido!")

    id_produto = int(input("Digite o id do produto que deseja: "))
    buscar_preco_por_id(id_produto)