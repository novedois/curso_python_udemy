try:
	file = open('def.txt', 'w+')
	file.write('Linha')
	file.seek(0)
	print(file.read())
finally:
	file.close()