from user import *
import re

class Fornecedor(User):

    lista_de_fornecedores = []
    
    def __init__(self, nome, telefone, empresa, endereco, regiao):
        super(Fornecedor, self).__init__(nome, telefone)
        self.empresa = empresa
        self.endereco = endereco
        self.regiao = regiao
    
    def altera_cadastro(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        
    @classmethod    
    def cria_usuarios(cls ,nome_arquivo):
        return super().cria_usuarios(nome_arquivo, Fornecedor.lista_de_fornecedores)
 
    def listar(self):
        i = 0
        while i < len(Fornecedor.lista_de_fornecedores):
            print(Fornecedor.lista_de_fornecedores[i].nome, 
                    Fornecedor.lista_de_fornecedores[i].empresa)
            i += 1 

    def remove(self):
        print('Executando remove')

    def adiciona(self):
        nome = input('Nome novo: ')
        telefone = input('Telefone novo: ')
        empresa = input('Empresa nova: ')
        endereco = input('Endereço: ')
        regiao = input('Região: ')
        arquivo = open('fornecedores.csv', 'a')
        arquivo.write(f'{nome}, {telefone}, {empresa}, {endereco}, {regiao}\r')
        arquivo.close()

    def listar_filtrado(self, regiao_informada):
        i = 0
        while i < len(Fornecedor.lista_de_fornecedores):
            if re.search(regiao_informada, Fornecedor.lista_de_fornecedores[i].regiao, re.IGNORECASE):
                print(Fornecedor.lista_de_fornecedores[i].nome)
            i += 1
            continue

