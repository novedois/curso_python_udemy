import enum


lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]

d1 = { x: y.upper() for x, y in lista }


d2 = { x: y * 5 for x, y in enumerate(range(5))}
d3 = { x for x in range(5)}

print(d1)
print(d2)
print(d3, type(d3))

d4 = { f'chave_{x}': x**2 for x in range(10) }
print(d4)