lista = [
    [ 'Marcos', 'João', 'Luiz' ],
    [ 'Maria', 'Ana', 'Clara' ],
    [ 'Du', 'Dudu', 'Edu' ]
]

enumerada = list(enumerate(lista))

print(enumerada[0][1][0])

for v1, v2 in enumerate(lista):
    print(v1, v2)

for v1, v2 in enumerate(lista, 55):
    print(v1, v2)

for v1 in enumerate(lista):
    print(v1)