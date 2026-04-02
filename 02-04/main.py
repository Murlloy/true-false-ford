while True:

    opcao = int(input("Bem Vindo ao Resolvedor de Exercicios!!!!\nData dos exercicios: 02/04/2026\n1 - Numeros Pares\n2 - Geração apartir do nascimentos\n3 - Eleições\n4 - Masculinos e Femininos\n5 - Idade Média\nDigite a opção que deseja resolver: "))

    if(opcao == 1):

        for i in range(101):
            if i % 2 == 0:
                print(f"{i} é par")
            
        break
        
    elif(opcao == 2):

        gen_beta = 0
        gen_alfa = 0
        gen_z = 0
        gen_y = 0
        gen_x = 0
        gen_baby = 0
        gen_silent = 0
        morto = 0

        pessoas = int(input("Digite quantas pessoas você quer saber a geração: "))

        for i in range(pessoas):
            print(f"{i + 1} pessoa")
            idade = int(input("Digite sua idade: "))

            ano_nascimento = 2026 - idade

            if(ano_nascimento >= 2025):
                print("====== GERAÇÃO BETA!!! =====")
                gen_beta += 1
            elif(ano_nascimento >=2011):
                print("====== GERAÇÃO ALFA!!! =====")
                gen_alfa += 1
            elif ano_nascimento >= 1997:
                print("====== GERAÇÃO Z!!! =====")
                gen_z += 1
            elif ano_nascimento >= 1981:
                print("====== GERAÇÃO Y!!! =====")
                gen_y += 1
            elif ano_nascimento >= 1965:
                print("====== GERAÇÃO X!!! =====")
                gen_x += 1
            elif ano_nascimento >= 1946:
                print("====== GERAÇÃO BABY BOOMER!!! =====")
                gen_baby += 1
            elif ano_nascimento >= 1925:
                print("====== GERAÇÃO SILENT!!! =====")
                gen_silent += 1
            else:
                print("====== VOCÊ JÁ MORREU!!! =====")
                morto += 1
                
        print(f"\n =========== TOTAL DE CADA GERAÇÃO ===========\n\nO total da GERAÇÃO BETA são: {gen_beta}")
        print(f"O total da GERAÇÃO ALFA são: {gen_alfa}")
        print(f"O total da GERAÇÃO Z são: {gen_z}")
        print(f"O total da GERAÇÃO Y são: {gen_y}")
        print(f"O total da GERAÇÃO X são: {gen_x}")
        print(f"O total da GERAÇÃO BABY BOOMER são: {gen_baby}")
        print(f"O total da GERAÇÃO SILENT são: {gen_silent}\n\n")
        
    elif(opcao == 3):

        vts_alston = 0
        vts_gabrinauan = 0
        vts_bolsonaro = 0

        print("======== BEM VINDO AO CONTADOR DE VOTOS =========\n\n1 - Alston Dificil Nome\n2 - Gabriel e Nauan\n3 - Bolsonaro\n")

        eleitores = int(input("Digite o quanto de eleitores votarão: "))

        for eleitor in range(eleitores):
            voto = int(input(f"Candidato n{eleitor+1} --- Quem você vai votar?\n\nAperte 4 para rever os eleitores\n\n:"))

            if(voto == 1):
                vts_alston += 1
                print("\nVoto no Alston Contabilizado!!!\n")
            elif voto == 2:
                vts_gabrinauan += 1
                print("\nVoto no Gabriel e Nauan Contabilizado!!!\n")
            elif voto == 3:
                vts_bolsonaro += 1
                print("\nVoto no Bolsonaro Contabilizado!!!\n")
            elif voto == 4:
                voto = int(input(f"\n\n1 - Alston Dificil Nome\n2 - Gabriel e Nauan\n3 - Bolsonaro\n\nQuem você vai votar?\n\n:"))

        participantes = [vts_alston,vts_bolsonaro,vts_gabrinauan]
        participantes.sort()

        if(vts_alston > vts_bolsonaro and vts_alston > vts_gabrinauan):
            ganhador = "Alston"
        elif vts_bolsonaro > vts_alston and vts_bolsonaro > vts_gabrinauan:
            ganhador = "Bolsonaro"
        elif vts_gabrinauan > vts_alston and vts_gabrinauan > vts_bolsonaro:
            ganhador = "Gabriel e Nauan"
        else:
            ganhdor = "Empate"

        if(ganhador == "Empate"):
            print("========== EMPATE ========")
            print("Obrigado a todos os candidatos!!")
        else:
            ganhador.upper()
            print(f"======= GANHADOR FOI: {ganhador} ========\n")
            print(f"Votos Totais do ganhador: {participantes[2]}\n")

    elif (opcao == 4):

        total_grupo = int(input("Digite o total de pessoas no grupo: "))
        sexo_f = 0
        sexo_m = 0

        for pessoa in range(total_grupo):

            while True:
                print(f"\n{pessoa + 1} Pessoa!!\n")
                sexo = input("Qual o seu sexo? m ou M (Masculino) e f ou F para (Feminino)\n: ")

                sexo = sexo.lower()
                
                if(sexo == "m" or sexo == "masculino"):
                    sexo_m += 1
                    print("Sexo Masculino Contabilizado!")
                    break;
                elif(sexo == "f" or sexo == "feminino"):
                    print("Sexo Feminino Contabilizado!")
                    sexo_f += 1
                    break
                else:
                    print("\n Valor invalido \n")
        
        print(f"O Total de Sexos Masculinos no grupo são: {sexo_m}")
        print(f"O Total de Sexos Femininos no grupo são: {sexo_f}")

    elif(opcao == 5):

        total_grupo = int(input("Digite o total de pessoas no grupo: "))
        sexo_f = 0
        sexo_m = 0

        idade_m = 0
        idade_f = 0
        idade_grupo = 0

        for pessoa in range(total_grupo):

            while True:
                print(f"\n{pessoa + 1} Pessoa!!\n")
                sexo = input("Qual o seu sexo? m ou M (Masculino) e f ou F para (Feminino)\n: ")
                idade = int(input("Digite sua Idade: "))

                sexo = sexo.lower()
                
                if(sexo == "m" or sexo == "masculino"):
                    print("Sexo Masculino Contabilizado!")
                    sexo_m += 1
                    idade_m += idade
                    idade_grupo += idade
                    break;
                elif(sexo == "f" or sexo == "feminino"):
                    print("Sexo Feminino Contabilizado!")
                    sexo_f += 1
                    idade_f += idade
                    idade_grupo += idade
                    break
                else:
                    print("\n Valor invalido \n")

        media_grupo = idade_grupo / total_grupo
        media_m = idade_m / sexo_m
        media_f = idade_f / sexo_f
        
        print(f"O Total de Sexos Masculinos no grupo são: {sexo_m}")
        print(f"O Total de Sexos Femininos no grupo são: {sexo_f}")

        print(f"Idade Média do Grupo: {media_grupo}")
        print(f"Idade Média dos Homens: {media_m}")
        print(f"Idade Média das Mulheres: {media_f}")

    opcao = input("Deseja Continuar? 1 - Sim e 2 - Não\n:")
    if(opcao == "2"):
        break;