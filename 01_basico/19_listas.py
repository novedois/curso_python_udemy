'''
Fatiamento
append, insert, pop, del, clear, extend
min, max
range
'''

lista = [ 1, 2, 3, 4, 'Filipe', True, 3.3 ]
print(f'\nLista: {lista}\n')

for item in lista:
    print(f'Item: {item} || Tipo: {type(item)}')

print(f'\nlista[0]: {lista[0]}')
print(f'lista[1]: {lista[1]}')
print(f'lista[2]: {lista[2]}')
print(f'lista[4][0]: {lista[4][0]}\n')

lista[6] = 'Mudei para string!'

print(f'lista[6] modificada: {lista}')

# Fatiamento

print('\n* * Fatiamento * *\n')

print(f'lista[0:3]..: {lista[0:3]}')
print(f'lista[0:4]..: {lista[0:4]}')
print(f'lista[:2]...: {lista[:2]}')
print(f'lista[-1]...: {lista[-1]}')
print(f'lista[::2]..: {lista[::2]}')
print(f'lista[::-1].: {lista[::-1]}')

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_3 = lista_1 + lista_2

print(f'''
lista_1: {lista_1}
lista_2: {lista_2}
lista_3 (lista_1 + lista_2): {lista_3}''')

# Extend, append, insert

lista_1.extend(lista_2)
lista_1.extend('a')

print(f'''
lista_1.extend(lista_2)
lista_1.extend('a')
lista_1: {lista_1}''')

lista_2.append(lista_1)
lista_2.append('d')

print(f'''
lista_2.append(lista_1)
lista_2.append('d')
lista_2: {lista_2}''')

lista_3.insert(0, 'banana')
lista_3.insert(3, 'macaco')

print(f'''
lista_3.insert(0, 'banana')
lista_3.insert(3, 'macaco')
lista_3: {lista_3}''')

# Pop e del

print(f'\nlista_2: {lista_2}\nlista_3: {lista_3}')

lista_3.pop()
del(lista_2[1:4])

print(f'''
lista_3.pop()
del(lista_2[1:4])

lista_2: {lista_2}
lista_3: {lista_3}''')

# Min e Max

lista_5 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'''
lista_5: {lista_5}
max(lista_5): {max(lista_5)}
min(lista_5): {min(lista_5)}''')

lista_6 = list(range(1,10))
print(f'''
lista_6 = list(range(1, 10))
lista_6: {lista_6}
''')

for valor in lista_6:
    print(f'x -> {valor}; x * 2 -> {valor * 2}')

print()