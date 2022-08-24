lista = [ 'Luiz', 'João', 'Maria' ]

# Associa os índices na ordem colocada
n1, n2, n3 = lista

print(n2)

lista_2 = [ 'João', 'Maria', 'Pedro', 'Carlos', 'Ana', 'Clara', 'Alberto' ]
m1, m2, *outra_lista, ultimo_da_lista = lista_2
*mais_uma_lista, x1, x2, x3 = lista_2

print(m1, m2)
print(outra_lista)
print(ultimo_da_lista)

print(mais_uma_lista)
print(x1)
print(x2)
print(x3)
