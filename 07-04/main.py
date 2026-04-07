
opcao = int(input("1 - Dicionarios de Livros\n" \
"2 - Dicionario de um Aluno\n" \
"3 - 3 produtos e preços \n" \
"\nDigite o exercicio que deseja resolver: "))

if opcao == 1 :
    # livro autor e ano

    livros= []

    for i in range(3):

        print(f"======== Configuração do {i + 1} Livro ===========")

        livro = {
            "nome_do_livro" : "",
            "autor" : "",
            "ano": ""
        }

        livro["nome_do_livro"] = input("Digite o Nome do Livro: ")
        livro["autor"] = input("Digite o Autor do Livro: ")
        livro["ano"] = input("Digite o Ano de Lançamento do Livro: ")

        livros.append(livro)
        print("Livro Cadastrado!!")

    i = 1

    for l in livros:
        print(f"Nome do {i} Livro: {l["nome_do_livro"]}")
        i+= 1



elif opcao == 2:
    # aluno com nome idade e curso

    aluno = {
        "nome" : "",
        "idade": "",
        "curso": ""
    }

    aluno["nome"] = input("Qual o seu nome: ")
    aluno["idade"] = input("Qual a sua idade: ")
    aluno["curso"] = input("Qual o seu curso: ")

    print(f"Nome: {aluno["nome"]}")
    print(f"Idade: {aluno["idade"]} anos")
    print(f"Curso: {aluno["curso"]}")

elif opcao == 3:
    # 3 produtos mostre o preço do primeiro produto e remova o produto 2 e mostre o dicionario
    
    produtos = []


    for i in range(3):

        produto = {
            "nome_produto": "",
            "preco": "",
            "cor": ""
        }

        print(f"======= Configuração do {i + 1} Produto ==========")

        produto["nome_produto"] = input("Digite o Nome do Produto: ")
        produto["preco"] =  input("Digite o Preço do Produto: ")
        produto["cor"] = input("Digite a cor do Produto: ")

        produtos.append(produto)

    print("======== Configurações do Primeiro Produto ===========" \
    f"\nProduto: {produtos[0]["nome_produto"]}" \
    f"\nPreço: {produtos[0]["preco"]}" \
    f"\nCor: {produtos[0]["cor"]}" 
    )

    print("\n ===== Lista atualizada sem o segundo produto =====")
    produtos.pop(1)
    
    i = 1

    for l in produtos:
        print(f"Produto {i}: {l["nome_produto"]}")
        i+= 1

    