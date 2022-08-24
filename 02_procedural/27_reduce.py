from functools import reduce
from dados import produtos, pessoas, lista


soma_lista = reduce(
    lambda acumulador, item_lista: 
        item_lista + acumulador, 
        lista, 
        0
)

soma_lista_2 = sum(lista)
print(soma_lista)
print(soma_lista_2)

# Soma preços dos produtos
soma_precos = reduce(
    lambda acumulador, produto: 
        produto['preco'] + acumulador, 
        produtos, 
        0
)

print(soma_precos)
print(soma_precos / len(produtos))

# Soma e média de idades
soma_idades = reduce(
    lambda acumulador, pessoas: 
        acumulador + pessoas['idade'], 
        pessoas, 
        0
)

print(soma_idades)
print(f'{(soma_idades / len(pessoas)):.2f}')

