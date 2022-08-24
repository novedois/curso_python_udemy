nome = input('Qual é o seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada')

print(nome or 'Você não digitou nada')

# Vai até o primeiro valor verdadeiro
print(nome or False or 0 or 'Você não digitou nada' or 'Outra')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

# Retorna a variável f pois é a primeira com valor (entendido como true)
variavel = a or b or c or d or e or f or g

print(variavel)