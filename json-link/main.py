import json

#function createUser

def createUser(username, password):
    newUser = {
        "username": username,
        "senha": password
    }

    #tentativa de ler o arquivo

    try:
        with open("users.json", "r") as arquivo:
            dados = json.load(arquivo)
    except:
        print("tentativa falha de ler \nCriando uma nova tabela....")
        dados = []

    dados.append(newUser)

    with open("users.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def verificarLogin(username, password):

    try:
        with open("users.json", "r") as arquivo:
            dados = json.load(arquivo)
    except:
        print("tentativa falha de ler \nCriando uma nova tabela....")
        dados = []

    for user in dados:

        if (user["username"] == username and user["senha"] == password):
            return True
        return False

def Login():
    login = input("Digite o username: ")
    password = input("Digite a senha: ")

    if (verificarLogin(login, password)):
        print("Sistema acessado!")



print("Bem vindo ao logador com json!!" \
"\n1 - Logar" \
"\n2 - Cadastrar" \
"\n3 - Sair")

opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        Login()
        
    case 2:
        Register()

# usuario = {
#     "username": "",
#     "senha": ""
# }

# username = input("What's your name?")
# password = input("Place your best password: ")

# def criarUsuario(username, password):
#     newUser = usuario(username, password)
#     with open("users.json", "w"):
#         json.dump(newUser, arquivo)


# with open("users.json", "r") as arquivo:
#     dados = json.load(arquivo)

# criarUsuario(username, password)

# print(dados)

# arquivo.close()

# # with open('users.json') as arquivo:
# #     dados = json.load(arquivo)

# # print(dados)