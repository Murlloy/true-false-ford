
import random

nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))

permissao = input('você tem permissão?? (Sim) ou (Não) \n').upper() == 'SIM'

if(permissao == False) and (idade < 18):
    desejo = input('Deseja forjar uma permissão? 1 - Sim 2 - Não\n')
    if(desejo == '1'):
        mae = input('Qual o nome da sua mãe? \n')

        if(mae == nome+'ana'):
            permissao = True
            print('Nome da Mãe Correto!!')
        else:
            print(f'Nome da mãe incorreto o nome é {nome}ana')
        

if idade >= 18 or permissao:
    print('Acesso Concebido')
else:
    print('Acesso Negado')

