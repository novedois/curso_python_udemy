# Função sem retorno explícito, devolve um none

def funcao(var):
    return var

a = funcao('Oie')
print(a)

def divisao(num_1, num_2):
    if num_2 > 0:
        return num_1 / num_2
    return 'Conta inválida'

divide_1 = divisao(5, 2)
divide_2 = divisao(2, 0)

print(divide_1)
print(divide_2)

def dumb():
    return 1

db = dumb()
print(db, type(db))

def imprime(var):
    print(var)

def oxe():
    return imprime

oxe()('Imprimindo de um jeito estranho')

def abuble():
    return ('Filipe', 'Azoubel')

var = abuble()
print(var[1], type(var))