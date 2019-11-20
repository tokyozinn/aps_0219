from fornecedor import *
import re
import csv

def menu_de_escolha():
    escolha = input("""Você deseja:
                    \n- [1] Procurar locais de descarte;
                    \n- [2] Acessar como fornecedor   
                    \n- [3] Acessar como admin
                    \n- [0] Fechar
                    \n>>> """)
    return escolha

def mensagem_entrada_cliente(nome):
    print(f'Bem-vindo {nome.title()}! Nosso programa te mostra os pontos de descarte mais próximos de você!')
    print('Nós cobrimos as regiões do Swift, Taquaral, Barão Geraldo, Vila Industrial, Campo Grande e Centro!')

def cria_lista_fornecedores(arquivo):
    
    try:
        lista = Fornecedor.lista_de_fornecedores = []
        Fornecedor.cria_usuarios(Fornecedor, arquivo, lista)
    except:
        Fornecedor.limpa_arquivo(Fornecedor, arquivo)

escolha = ""

while(escolha != "0"):

    cria_lista_fornecedores('fornecedores.csv')

    escolha = menu_de_escolha()

    if escolha == "1":

        nome = input('Qual seu nome? >>> ')

        while escolha == "1":
            
            mensagem_entrada_cliente(nome)

            bairro = Fornecedor.captura_bairro(Fornecedor)

            if "!!" not in bairro:
                print(f'\nProcurando locais de descarte na região {bairro}...\n')
            else:
                print('****************ERRO NA RESPOSTA****************')
                break
            Fornecedor.listar_filtrado(Fornecedor, bairro)
            print('Deseja procurar outra região?')
            escolha = input("""\n- [1] SIM
                               \n- [2] VOLTAR
                               \n- [0] FECHAR >>> """)
    elif escolha == "2":
        novo = input("""Você é fornecedor novo? 
                        \n- [Y] SIM 
                        \n- [N] NÃO >>> """)
        if novo == "Y" or novo == 'y':
            Fornecedor.adiciona(Fornecedor)
        else:
            Fornecedor.altera_cadastro(Fornecedor, Fornecedor.lista_de_fornecedores)
    elif escolha == "3":
        print('Acessando como admin...')
        escolha_do_adm = input("""Você deseja 
                                \n- [1] Listar fornecedores
                                \n- [2] Adicionar fornecedor
                                \n- [3] Remover fornecedor >>> """)
        if escolha_do_adm == "1":
            Fornecedor.listar(Fornecedor)
        elif escolha_do_adm == "2":
            Fornecedor.adiciona(Fornecedor)
        elif escolha_do_adm == "3":
            Fornecedor.remove(Fornecedor, Fornecedor.lista_de_fornecedores)
        else:
            continue

print("\n!!!!!!!!!!!!!!!!!!!\nFechando programa...\n!!!!!!!!!!!!!!!!!!!")

