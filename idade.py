
dia_atual = 25
mes_atual = 3
ano_atual = 2026

faixa_etaria = 'nenhuma'

signo = 'pelé'

while True:
    try:
        dia_nascimento = int(input('Digite o dia do seu nascimento: '))
        if(dia_nascimento > 31 or dia_nascimento <= 0):
            print('dia invalido')
        else:
            break
    except ValueError:
        print('dia invalido')


while True:
    try:
        mes_nascimento = int(input('Digite o mes do seu nascimento: '))
        if(mes_nascimento <= 0 or mes_nascimento >= 12):
            print('mes invalido')
        else:
            break
    except ValueError:
        print('mes invalido')


while True:

    try:
        ano_nascimento = int(input('Digite o ano do seu nascimento: '))
        if(ano_nascimento <= 0 or ano_nascimento >= ano_atual):
            if(mes_nascimento >= mes_atual):
                if(dia_atual == dia_nascimento):
                    break
                if(dia_atual > dia_nascimento):
                    print('ano invalido')
                print('ano invalido')
            else:
                print('ano invalido')
        else:
            break

    except ValueError:
        print('ano invalido')

idade = ano_atual - ano_nascimento


# idade = ano_nascimento - ano_atual


# if(mes_nascimento == 1):
#     if(dia_nascimento <= 12):
#         signo = 'capricornio'
#     else:
#         print('você é gabriel')

# if(mes_nascimento == 12):
#     if(dia_nascimento >= 22):
#         print(' você é nauan')
#     else:
#         print(' você é sauan')


if(mes_atual <= mes_nascimento):
    if(dia_atual <= dia_nascimento and mes_atual == mes_nascimento):
        if(dia_atual == dia_nascimento):
            print('feliz aniversario!!')
            print(f'sua idade: {idade}')
        else:
            print('é seu mês de aniversario!!! parabens')
            print(f'sua idade: {idade - 1}')
    
    elif(dia_atual >= dia_nascimento and mes_atual == mes_nascimento):
        print('já passou seu aniversario!')
        print(f'sua idade: {idade}')

    else:
        print(f'seu aniversario é dia {dia_nascimento} de {mes_nascimento}')
        print(f'sua idade: {idade - 1}')
        

if(mes_atual > mes_nascimento):
    print('já passou seu aniversario!')

# verificação de faixa etaria

if(idade <= 12):
    faixa_etaria = 'Criança'
elif(idade <= 17):
    faixa_etaria = 'Adolescente'
elif(idade <= 25):
    faixa_etaria = 'Adulto JR'
elif(idade <= 35):
    faixa_etaria = 'Adulto R'
elif(idade <= 60):
    faixa_etaria = 'Adulto Senior'
elif(idade <= 100):
    faixa_etaria = 'Idoso'
else:
    faixa_etaria = 'Pé no caixão'

print(faixa_etaria)

# if(dia_atual == dia_nascimento and mes_atual == mes_nascimento):
#     print('hoje é seu aniversario!! parabens')
#     print(f'sua idade: {-idade}')

# if(mes_atual <= mes_nascimento):

#     if(dia_atual < dia_nascimento):
#         print('seu aniversario ainda não passou')
#         print(f'vai ser dia {dia_nascimento} no mês de {mes_nascimento} de {ano_atual}')
#         print(f'sua idade: {-idade-1}')
#     if(dia_atual >= mes_nascimento and mes_nascimento <= mes_atual):
#         print(f'você tem {-idade}')
#         print(f'seu aniversario foi dia {dia_nascimento} de {mes_nascimento} de {ano_atual}')

    
# if(mes_atual >= mes_nascimento):
#     print(f'você tem {-idade}')
#     print(f'seu aniversario foi dia {dia_nascimento} de {mes_nascimento} de {ano_atual}')