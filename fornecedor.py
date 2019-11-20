import re
import csv

class Fornecedor:
    
    def __init__(self, chave_id, nome, telefone, empresa, bairro, endereco):
        self.chave_id = chave_id
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.bairro = bairro
        self.endereco = endereco
    
    def cria_usuarios(self, nome_arquivo, lista):
            with open(nome_arquivo, 'r') as arquivo:
                for user in arquivo:
                    valores = user.split(',')
                    if user != "\n":
                        lista.append(self(*valores))
            arquivo.close()
            return lista

    def altera_cadastro(self, lista):
        id_a_alterar = input('Qual seu ID? >>> ')
        i = 0
        achou = False
        while i < len(lista):
            if id_a_alterar == lista[i].chave_id:
                lista[i].nome = input("Nome novo >>> ")
                lista[i].telefone = input("Telefone novo >>> ")
                lista[i].empresa = input("Empresa nova >>> ")
                lista[i].bairo = lista[i].captura_bairro()
                lista[i].endereco = input("Endereço novo >>> ") + "\n"
                achou = True
            i += 1
        if achou:
            with open('fornecedores.csv', 'w') as f:
                for item in lista:
                    f.write(f'{item.chave_id},{item.nome},{item.telefone},{item.empresa},{item.bairro},{item.endereco}') 
        print(lista)
 
    def listar(self):
        i = 0
        while i < len(Fornecedor.lista_de_fornecedores):
            print(f"""ID -> {Fornecedor.lista_de_fornecedores[i].chave_id} Empresa -> {Fornecedor.lista_de_fornecedores[i].empresa}\n""")

            i += 1     
    
    def remove(self, lista):

        id_a_remover = input('Digite o ID do fornecedor que deseja remover >>> ')
        i = 0
        achou = False
        while i < len(lista):
            if lista[i].chave_id == id_a_remover:
                print(i)
                lista.pop(i)
                achou = True
            i += 1
        if achou:
            with open('fornecedores.csv', 'w') as f:
                for item in lista:
                    f.write(f'{item.chave_id},{item.nome},{item.telefone},{item.empresa},{item.bairro},{item.endereco}') 
        print(lista)

    def captura_bairro(self):

        bairro = ''
        while bairro == '':
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
                bairro = ''
        return bairro.title()

    def adiciona(self):
        nome = input('Nome novo: ')
        telefone = input('Telefone novo: ')
        empresa = input('Empresa nova: ')
        chave_id = 1
        for user in Fornecedor.lista_de_fornecedores:
            id_auxiliar = int(user.chave_id)
            if  id_auxiliar >= chave_id:
                chave_id =  id_auxiliar + 1
        
        bairro = Fornecedor.captura_bairro(self)
        endereco = input('Endereço: ')
        with open('fornecedores.csv', 'a') as arquivo:
            arquivo.write(f'{chave_id},{nome},{telefone},{empresa},{bairro},{endereco}\r')
            arquivo.close()
        print(f"\nParabéns {nome}! Seu cadastro foi realizado com sucesso! Seu ID é: {chave_id}\n")

    def listar_filtrado(self, bairro_informado):
        i = 0
        while i < len(Fornecedor.lista_de_fornecedores):

            if re.search(bairro_informado, Fornecedor.lista_de_fornecedores[i].bairro, re.IGNORECASE):
                empresa = Fornecedor.lista_de_fornecedores[i].empresa
                telefone = Fornecedor.lista_de_fornecedores[i].telefone
                endereco = Fornecedor.lista_de_fornecedores[i].endereco
                print(f"""Empresa -> {empresa}\nTelefone -> {telefone}\nEndereço -> {endereco}\n""")
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
