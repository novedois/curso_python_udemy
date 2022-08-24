# listas, tuplas, str -> squences -> iteráveis

nome = 'Filipe Azoubel'

for letra in nome:
    print(letra)

print('#' * 80)

iterador = iter(nome)

print(iterador)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

print("\nAqui tem um for! Valores já foram iterados :o\n")
for valor in iterador:
    print(valor)

gerador = ( letra for letra in nome )

print(gerador)
print(type(gerador))

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('\nOlha o for do gerador\n')

for l in gerador:
    print(l)