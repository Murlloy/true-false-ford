while True:

    tipo_gasolina = input("Qual gasolina você quer usa? A - (Álcool) e G - (Gasolina)\n\n")
    tipo_gasolina = tipo_gasolina.upper()
    gasolina = False

    if(tipo_gasolina == "G"):
        gasolina = True
        break
    elif(tipo_gasolina == "A"):
        gasolina = False
        break
    else:
        print("\n == Valor Invalido!! ==\n")

litros = float(input("Digite o valor de gasolina que você vai querer: "))

if(gasolina == True):

    preco = 5.50

    if(litros > 20):
        desconto = 6.00
    else:
        desconto = 4.00
    
    
    print("\n ========== Gasolina Escolhido!! ======= \n")

else:

    preco = 3.89

    if(litros > 20):
        desconto = 5.00
    else:
        desconto = 3.00

    print("\n ========== Álcool Escolhido!! ======= \n")

preco_total = preco * litros
preco_final = preco_total * (1 - (desconto/100))


print(f"Preço do Combustivel R${preco:.2f}\nTotal de Litros: {litros} Litros\nPreço sem desconto: R${preco * litros}\nDesconto Aplicado de {desconto}%\n\nPreço Final a Ser pago: R${preco_final:.2f}\n\n========================")
