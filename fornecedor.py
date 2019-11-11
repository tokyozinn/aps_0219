import re

class Fornecedor:
    
    def __init__(self, nome, telefone, empresa, id, bairro, endereco):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.id = id
        self.bairro = bairro
        self.endereco = endereco
    
    def cria_usuarios(self, nome_arquivo, lista):
            arquivo = open(nome_arquivo, 'r')
            i = 0
            for user in arquivo:
                valores = user.split(',')
                lista.append(self(*valores))
                i += 1
            arquivo.close()
            return lista

    def altera_cadastro(self):
        id = input('Qual seu id?')
        print(Fornecedor.lista_de_fornecedores[0])
        for x in Fornecedor.lista_de_fornecedores:
            if (x.id == id):
                print('bataaaaaaaaaaaaaaaaaaaataaaaaaaaaaaaa')
                x.nome = input('nome novo')
                x.telefone = input('telefone novo')
                x.empresa = input('empresa nova')
            else:
                print('batatinha quando nasce............')
 
    def listar(self):
        i = 0
        while i < len(Fornecedor.lista_de_fornecedores):
            print(Fornecedor.lista_de_fornecedores[i].nome, 
                    Fornecedor.lista_de_fornecedores[i].empresa,
                    Fornecedor.lista_de_fornecedores[i].id)
            i += 1 

    def remove(self):
        print('Executando remove')

    def captura_bairro(self):
        bairro = input("""Bairro: 
            \r[1] - Swift
            \r[2] - Centro
            \r[3] - Taquaral
            \r[4] - Barão Geraldo
            \r[5] - Vila Industrial
            \r[6] - Campo Grande >>> """)

        if bairro == "1":
            bairro = "swift"
        elif bairro == "2":
            bairro = "centro"
        elif bairro == "3":
            bairro = "taquaral"
        elif bairro == "4":
            bairro = "barão geraldo"
        elif bairro == "5":
            bairro = "vila industrial"
        elif bairro == "6":
            bairro = "campo grande"
        else:
            bairro = "!!"
        return bairro

    def adiciona(self):
        nome = input('Nome novo: ')
        telefone = input('Telefone novo: ')
        empresa = input('Empresa nova: ')
        id = str(len(Fornecedor.lista_de_fornecedores) + 1)
        bairro = Fornecedor.captura_bairro()


        endereco = input('Endereço: ')
        with open('fornecedores.csv', 'a') as arquivo:
            arquivo.write(f'{nome}, {telefone}, {empresa}, {id}, {bairro}, {endereco}\r')
            arquivo.close()
        print()

    def listar_filtrado(self, bairro_informado):
        i = 0
        while i < len(Fornecedor.lista_de_fornecedores):
            if re.search(bairro_informado, Fornecedor.lista_de_fornecedores[i].bairro, re.IGNORECASE):
                print(Fornecedor.lista_de_fornecedores[i].nome)
            i += 1
            continue

    def limpa_arquivo(cls, nome_arquivo):
        arquivo_erro = open('fornecedores.csv', 'r')
        texto_com_erro = arquivo_erro.read()
        arquivo_erro.close()

        arquivo_backup = open('erros.csv', 'w')
        arquivo_backup.write(texto_com_erro)
        arquivo_backup.close()

        arquivo_novo = open('fornecedores.csv', 'w')
        arquivo_novo.write('')
        arquivo_novo.close()

class Lista:

    def __init__(self, nome, fornecedores):
        self.nome = nome
        self.fornecedores = fornecedores

    def __getitem__(self, item):
        return self.fornecedores[item]