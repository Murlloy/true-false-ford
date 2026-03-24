
salario = float(input('digite o seu salario: '))
anos_trabalhados = int(input('digite seus anos de empresa: '))

if(anos_trabalhados >= 2 and salario <= 3000):
    print('Bonus Concebido')
else:
    print('Não terá Bonus')