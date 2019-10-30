from user import *
from fornecedor import *
from cliente import *

escolha = ""
while(escolha != "0"):

    Fornecedor.cria_usuarios('fornecedores.csv')

    escolha = input("""Você deseja:
                    \n- [1] Procurar locais de descarte;
                    \n- [2] Acessar como fornecedor   
                    \n- [3] Acessar como admin
                    \n- [0] Fechar
                    \n>>> """)

    if escolha == "1":
        while escolha == "1":
            regiao = input('Digite em qual região de Campinas quer encontrar pontos de descarte: ')
            print(f'*******\n\nProcurando locais de descarte na região {regiao}...\n\n********\n')
            Fornecedor.listar_filtrado(Fornecedor, regiao)
            print('Deseja procurar outra região?')
            escolha = input("""\n- [1] SIM
                               \n- [0] FECHAR >>> """)
    elif escolha == "2":
        novo = input("""Você é fornecedor novo?\n 
                        \n- [Y] SIM 
                        \n- [N] NÃO""")
        if novo == "Y" or "y":
            Fornecedor.adiciona(Fornecedor)
        else:
            Fornecedor.altera_cadastro()
    elif escolha == "3":
        print('Acessando como admin...')
        escolha_do_adm = input("""Você deseja 
                                \n- [1] Listar fornecedores
                                \n- [2] Adicionar fornecedor
                                \n- [3] Remover fornecedor""")
        if escolha_do_adm == "1":
            Fornecedor.listar(Fornecedor)
        elif escolha_do_adm == "2":
            Fornecedor.adiciona(Fornecedor)
        elif escolha_do_adm == "3":
            Fornecedor.remove()
        else:
            continue



print("\n!!!!!!!!!!!!!!!!!!!\nFechando programa...\n!!!!!!!!!!!!!!!!!!!")

