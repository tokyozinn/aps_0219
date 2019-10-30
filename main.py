from user import *
from fornecedor import *
from cliente import *

escolha = ""
while(escolha != "0"):

    Fornecedor.cria_usuarios('fornecedores.csv')

    escolha = input("""Você deseja:
                    \n- [1]Procurar locais de descarte;
                    \n- [2]Acessar como fornecedor   
                    \n- [3]Acessar como admin
                    \n- [0]Fechar
                    \n>>> """)

    if escolha == "1":
        while escolha == "1":
            regiao = input('Digite em qual região de Campinas quer encontrar pontos de descarte: ')
            print(f'*******\n\nProcurando locais de descarte na região {regiao}...\n\n********\n')
            print('Executando Fornecedores.listar()')
            print('Deseja procurar outra região?')
            escolha = input('Digite [1] para SIM, digite [0] para FECHAR >>> ')
    elif escolha == "2":
        novo = input('Você é fornecedor novo? [Y] or [N]')
        if novo == "Y" or "y":
            nome = input('Qual seu nome?')
            telefone = input('Qual seu telefone?')
            empresa = input('Qual sua empresa?')
            Fornecedor.__init__(Fornecedor, nome=nome, telefone=telefone, empresa=empresa)
        else:
            Fornecedor.altera_cadastro()
    elif escolha == "3":
        print('Acessando como admin...')
        escolha_do_adm = input('Você deseja [1]Listar fornecedores\n[2]Adicionar fornecedor\n[3]Remover fornecedor')
        if escolha_do_adm == "1":
            Fornecedor.listar(Fornecedor)
        elif escolha_do_adm == "2":
            Fornecedor.adiciona(Fornecedor)
        elif escolha_do_adm == "3":
            Fornecedor.remove()
        else:
            continue



print("\n!!!!!!!!!!!!!!!!!!!\nFechando programa...\n!!!!!!!!!!!!!!!!!!!")

