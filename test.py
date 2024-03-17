def xpto():
    nomes = ['turing', 'llace', 'hooper']
    senhas = ['tmachine', 'anengine', "business"]
    login = input("Usuário: ")
    if login in nomes:
        index = nomes.index(login)
        senha = input("senha: ")
        if senha == senhas[index]:
           print("Bem-vindo!")
    else:
        print("Login ou senha incorreto") 


if __name__ == '__main__':
    xpto()
