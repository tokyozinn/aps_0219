class User():

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    @classmethod
    def cria_usuarios(cls, nome_arquivo):
        users = []
        arquivo = open(nome_arquivo, 'r')
        for user in arquivo:
            valores = user.split(',')
            users.append(cls(*valores))
            print(users)
        arquivo.close()
        return users

class Fornecedor(User):

    def __init__(self, nome, telefone, empresa):
        super(Fornecedor, self).__init__(nome, telefone)
        self.empresa = empresa
    
    def altera_cadastro(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        