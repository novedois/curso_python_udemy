# Maneira mais pythonica - gerenciador de contexto

with open('ghi.txt', 'w+') as file:
	file.write('Linha 1\n')
	file.write('Linha 2\n')
	file.write('Linha 3')

	file.seek(0)
	print(file.read())

print("\n#########################\n")

with open('abc.txt', 'r') as file:
	print(file.read())

print("\n#########################\n")

with open('abc.txt', 'a+') as file:
	file.write('Outra linha\n')
	file.seek(0)
	print(file.read())