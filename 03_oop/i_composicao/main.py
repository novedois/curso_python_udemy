from classes import Cliente, Endereco

cliente_1 = Cliente('Luiz', 33)
cliente_1.insere_endereco('Belo Horizonte', 'MG')

cliente_2 = Cliente('Maria', 29)
cliente_2.insere_endereco('Recife', 'PE')
cliente_2.insere_endereco('Rio de Janeiro', 'RJ')

cliente_3 = Cliente('João', 19)
cliente_3.insere_endereco('São Paulo', 'SP')

print()
print(cliente_1.nome)
cliente_1.lista_enderecos()
del cliente_1

print()
print(cliente_2.nome)
cliente_2.lista_enderecos()

print()
print(cliente_3.nome)
cliente_3.lista_enderecos()

print('\n#######################################\n')


