class User():

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    @staticmethod
    def cria_usuarios(nome_arquivo):
        users = []
        arquivo = open(nome_arquivo, 'r')
        for user in arquivo:
            valores = user.split(',')
            users.append(User(*valores))
            print(users)
        arquivo.close()
        return users
