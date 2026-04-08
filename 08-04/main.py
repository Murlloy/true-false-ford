
opcao = int(input("1 - Contar Pares\n" \
"2 - Ao Cubo de numeros\n" \
"3 - Lista de Compras \n" \
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