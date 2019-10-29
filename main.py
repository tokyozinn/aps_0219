from user import *

lista = User.cria_usuarios('teste.csv')
print('Usuários cadastrados com sucesso!')
tamanho_lista = len(lista)
i = 0
while i < tamanho_lista:
    print(lista[i].nome)
    i+=1

