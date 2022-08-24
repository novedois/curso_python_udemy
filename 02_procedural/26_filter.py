from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

nova_lista = [ x for x in lista if x > 5 ]
print(nova_lista)


# Pega apenas os produtos que custam mais de 10 reais
nova_lista = filter(lambda p: p['preco'] > 30, produtos)

for produto in nova_lista:
    print(produto)

# Checa quem tem menos de 22 anos
nova_lista = filter(lambda p: p['idade'] < 22, pessoas)

for pessoa in nova_lista:
    print(pessoa)