from itertools import count

# Cuidado com loops infinitos
contador = count()

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

contador_2 = count(start=5)

print(next(contador_2))
print(next(contador_2))
print(next(contador_2))
print(next(contador_2))
print(next(contador_2))

contador_3 = count(start=3, step=0.1)

for valor in contador_3:
    print(round(valor, 2))

    if valor > 5:
        break

contador_4 = count(start=10, step=-1)

for valor in contador_4:
    print(valor)
    if valor <= 0:
        break

contador_5 = count()

lista = [ 'Filipe', 'Ana', 'Maria', 'Paulo' ]
lista = list(zip(contador_5, lista))

print(lista)