# Conjuntos
# Suportam apenas elementos únicos
# Não respeita a ordem
# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (todos os elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

s0 = {} # As chaves em branco NÃO criam um set, criam um dicionário

s1 = { 1, 2, 3, 4, 5 }
s2 = set()

s2.add(1)
s2.add(2)
s2.add(3)

# O update recebe um iterável e itera sobre este elemento
# Se uma string for passada, será dividida
s2.update('a')
s2.update('python')
s2.update(['filipe', 'azoubel'])

s2.discard(2)


print(s1)
print(s2)

for i in s1:
    print(i)

# O set é útil para remover elementos duplicados de uma lista
# (Os elementos ficarão fora de ordem)

l1 = [ 1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 'Filipe', 'Filipe', 7, 7, 9 ]

novo_set = set(l1)

print(novo_set)

print(list(novo_set))


conjunto_1 = { 1, 2, 3, 4, 5, 7 }
conjunto_2 = { 1, 2, 3, 4, 5, 6 }

print(f'\nConjunto_1: {conjunto_1}')
print(f'Conjunto_2: {conjunto_2}\n')

# Une os sets
conjunto_3 = conjunto_1 | conjunto_2

# Intersection (elementos que estão nos dois sets)
conjunto_4 = conjunto_1 & conjunto_2

# Difference (elementos apenas no set DA ESQUERDA)
conjunto_5 = conjunto_1 - conjunto_2

# Symmetric_difference ^ (elementos nos dois sets, mas não em ambos [diferentes e tal])
conjunto_6 = conjunto_1 ^ conjunto_2

print(f'''
union: {conjunto_3}
intersection: {conjunto_4}
difference: {conjunto_5}
symmetric_difference: {conjunto_6}
''')

# Você pode usar sets para verificar se listas diferentes com muitos elementos
# repetidos na verdade são iguais
l1 = [ 'luiz', 'filipe', 'ana', 'maria' ]
l2 = [ 'ana', 'maria', 'maria', 'maria', 'filipe', 'filipe', 'filipe', 'luiz' ]

set_l1 = set(l1)
set_l2 = set(l2)

print(set_l1 == set_l2)