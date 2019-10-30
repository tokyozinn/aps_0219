class User():

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    @classmethod
    def cria_usuarios(cls, nome_arquivo, lista):
        arquivo = open(nome_arquivo, 'r')
        i = 0
        for user in arquivo:
            valores = user.split(',')
            lista.append(cls(*valores))
            i += 1
        arquivo.close()
        return lista

    
