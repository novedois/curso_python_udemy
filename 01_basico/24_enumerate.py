print()

lista = [ 'meu', 'nome', 'é', 'filipe' ]

for index, valor in enumerate(lista):
    print(index, valor.capitalize())

print()

lista_2 = [
    [1, 'Luiz'],
    [3, 'João'],
    [5, 'Maria']
]


# É isso aqui que o enumerate faz ;-;
for indice, nome in lista_2:
    print(indice, nome)

print()

n1, n2, n3 = lista_2

print(lista_2)

print()
