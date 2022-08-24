'''
for para iteráveis e quando você sabe a quantidade de loops
range(start=0, stop, step=1)
'''


texto = 'Python'

for letra in texto:
    print(letra)

print()

for num in range(11):
    print(num)

print()

for num in range(5, 11):
    print(num)

print()

for num in range(20, 5, -1):
    print(num)

print()

for num in range(0, 101):
    if num % 8 == 0:
        print(num)

nova_string = ''

for letra in texto:
    if letra == 't':
        continue
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(texto)
print(nova_string)