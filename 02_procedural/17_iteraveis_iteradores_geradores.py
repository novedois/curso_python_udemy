
# Checa se as variáveis são iteráveis
lista = [ 0, 1, 2, 3, 4, 5 ]
string = [ 'Filipe', 'João', 'Marcelo' ]
numero = 12345

print(hasattr(lista, '__iter__'))
print(hasattr(string, '__iter__'))
print(hasattr(numero, '__iter__'))

# O for transforma a lista em um iterador
for i in lista:
    print(i)

# A lista por si só não é um iterador
print(hasattr(lista, '__next__'))

# Transforma a lista em um iterador
lista = iter(lista)
print(hasattr(lista, '__next__'))

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

# -- #

import sys
import time

def gera():
    
    for n in range(10):
        yield n
        time.sleep(0.1)
    

g = gera()

for v in g:
    print(v)

print(hasattr(g, '__next__'))
print(hasattr(g, '__iter__'))

def gera_2():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

g2 = gera_2()

print(next(g2))
print(next(g2))
print(next(g2))


lista = [ x for x in range(100000) ]
print(type(lista))
print(sys.getsizeof(lista))

lista = ( x for x in range(100000) )
print(sys.getsizeof(lista))
print(type(lista))


for i in range(10000):
    print(i)