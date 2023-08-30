login = input("Informe seu login: ")
senha = input("Informe sua senha: ")

while senha == login:
    print("Senha não pode ser igual ao login. ")
    login = input("Informe seu login: ")
    senha = input("Informe sua senha: ")

else:
    print("Seja Bem-Vindo. ")
