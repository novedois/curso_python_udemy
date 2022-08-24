t1 = (1, 2, 3, 'a', 'Filipe')

print(t1)
print(t1[2])
print(t1[-1])
print(t1[:2])
print(t1[2:])

# Você pode criar uma tupla sem os parênteses

t2 = 1, 2, 3, 'a', 'Azoubel'

print(t2)


# Cria tupla com um elemento
t3 = 1,

print(t3)

# Concatena tuplas
t4 = t1 + t2

print(t4)

# Desempacota
n1, n2, n3, *_, n10 = t4

print(n1)
print(n2)
print(n3)
print(*_)
print(n10)

# Multiplicando a tupla (a tupla em si, não os valores)

t5 = t4 * 5

print(t5)

# Tuplas não podem ser modificadas, você precisa transformar em uma lista
t6 = list(t1)
print(t6)