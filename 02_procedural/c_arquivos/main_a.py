file = open('abc.txt', 'w+')

file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

# Chama o cursor para o início do arquivo
file.seek(0, 0)

print('\nLendo linhas:\n')

print(file.read())

print('###################\n')

file.seek(0, 0)

print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

print('\n###################\n')

file.seek(0, 0)

# print(file.readlines()) -> imprime uma lista
for linha in file.readlines():
	print(linha, end='')

print('\n###################\n')

file.seek(0, 0)

for linha in file:
	print(linha, end='')


file.close()