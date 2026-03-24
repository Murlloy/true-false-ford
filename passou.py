
nome = input('Digite o nome do aluno: ')
nota = int(input('Nota final do aluno: '))
frequencia = float(input('Frequencia do aluno: '))

if(frequencia >= 75 or nota >= 7):
    print('Passou')
else:
    print('Virou Gabriel!!')