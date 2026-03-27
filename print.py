# numero = 88

# for i in range(numero, 0, -1):
#     if(i % 5 == 0):
#         print(f"{i} é par")
#     # else:
#     #     print(f"{i} é impar")


numero = int(input("Digite a tabuada que quer resolver: "))

for i in range(0, 11, 1):
    print(f"{numero} x {i} = {numero*i}")
