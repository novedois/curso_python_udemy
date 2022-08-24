l1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

l2 = [ variavel for variavel in l1 ]
l3 = [ variavel * 2 for variavel in l1 ]

# v1 roda 3 vezes antes de incrementar
l4 = [ (v1, v2) for v1 in l1 for v2 in range(3) ]

l5 = [ 'Filipe', 'Maria', 'Ana' ]
l6 = [ valor.replace('a', '@').upper() for valor in l5]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

l7 = [ (x, y) for x, y in tupla ]
l8 = [ (y, x) for x, y in tupla ]

print(l2)
print(l3)
# print(l4)
print(l6)
print(l7)
print(l8)

l9 = list(range(100))

l10 = [ valor for valor in l9 if valor % 2 == 0 if valor % 8 == 0 ]

l11 = [ valor if valor % 3 == 0 else 'Não é' for valor in l9 ]
print(l10)
print(l11)