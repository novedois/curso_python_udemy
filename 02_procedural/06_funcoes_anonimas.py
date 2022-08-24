# A função declarada e a função anônima (lambda) abaixo fazem a mesma coisa

def funcao(n1, n2):
    return n1 * n2

a = lambda x, y: x * y

var = funcao(2, 2)

print(a(2, 2))

lista = [
    [ 'P1', 13 ],
    [ 'P2', 6 ],
    [ 'P3', 100 ],
    [ 'P4', 91 ],
    [ 'P5', 55 ]
]

def func(item):
    return item[1]

lista.sort(key=func, reverse=True)
print(lista)

lista_2 = [
    [ 'P1', 13 ],
    [ 'P2', 6 ],
    [ 'P3', 100 ],
    [ 'P4', 91 ],
    [ 'P5', 55 ]
]

lista_2.sort(key=lambda item: item[1], reverse=True)
print(lista_2)

lista_3 = [
    [ 'P1', 13 ],
    [ 'P2', 6 ],
    [ 'P3', 100 ],
    [ 'P4', 91 ],
    [ 'P5', 55 ]
]

print(sorted(lista_3, key = lambda i: i[1]))
