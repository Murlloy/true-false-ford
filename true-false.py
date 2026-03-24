
usuarios = []

class usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password

    def bark(self):
        print(f'Diga Oi {self.username}')

def criarUsuario(username, password):
    usuarios.append(usuario(username,password))

def Login():

    username = input('Digite o Usuario: ')
    password = input('Digite a Senha: ')

    for u in usuarios:
        if(u.get_username() == username and u.get_password() == password):
            
            print('Logado Com Sucesso!!')
            return True
    
    print('Senha ou Usuarios Invalidos!!')
    return False
        
def verificarUsuario(username):

    for u in usuarios:
        if(u.get_username() == username):
            print('Existe um Usuario com esse nome!')
            return False
    
    print('Usuario Unico!')
    return True
        
def cadastrarUsuario():

    while True:

        username = input('Digite o Usuario: ')
        password = input('Digite a Senha: ')

        if(verificarUsuario(username) == True):
            criarUsuario(username, password)
            print('Usuario Cadastrado com Sucesso!!')
            break
        else:
            print('Tente Novamente')

criarUsuario('admin', 'admin')

while True:

    print('===== CYBER LOGIN 2026 =======')
    print('Bem Vindo ao CYBER LOGIN de Usuarios!!')

    print('1 - LOGIN' \
    '\n2 - CADASTRO' \
    '\n3 - Verificar Login' \
    '\n4 - Sair')

    opcao = int(input('Oque você deseja fazer? \n'))

    match opcao:
        case 1:
            if(Login()):
                break
        case 2:
            cadastrarUsuario()
        case 3:

            username = input('Qual o usuario: ')

            verificarUsuario(username)

        case 4:
            break