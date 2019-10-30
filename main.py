from user import *
from fornecedor import *
from cliente import *

escolha = ""
while(escolha != "0"):

    escolha = input("Você deseja:\n[1]Procurar locais de descarte;\n[2]Acessar como fornecedor\n[3]Acessar como admin\n[0]Fechar\n")

    if escolha == "1":
        print('Procurando locais de descarte na sua região...')
    elif escolha == "2":
        novo = input('Você é fornecedor novo? [Y] or [N]')
        if novo == "Y" or "y":
            print('Executando Fornecedor.cadastrar()')
        else:
            print('Executando Fornecedor.altera_cadastro()')
    elif escolha == "3":
        print('Acessando como admin...')
        escolha_do_adm = input('Você deseja [1]Listar fornecedores\n[2]Adicionar fornecedor\n[3]Remover fornecedor')
        if escolha_do_adm == "1":
            print('Listando todos os fornecedores... Fornecedor.listar()')
        elif escolha_do_adm == "2":
            print('Executando Fornecedor.adiciona_fornecedor()')
        elif escolha_do_adm == "3":
            print('Executando Fornecedor.remove_fornecedor()')
        else:
            continue



print("Fechando programa...")

