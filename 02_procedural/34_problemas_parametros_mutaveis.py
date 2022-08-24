# Mutável - listas, dicionários
# Imutável - tuplas, strings, números, True, False, none

# Mudamos a lista para o None, que é imutável (era um [])
def lista_de_clientes(clientes_iteravel, lista = None):
	# Se a lista for none, criamos uma nova lista []
	if lista is None:
		lista = []	
	lista.extend(clientes_iteravel)
	return lista

clientes_1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes_2 = lista_de_clientes(['Zico', 'Garrincha', 'Pelé'])
clientes_3 = lista_de_clientes(['José'])

print(clientes_1)
print(clientes_2)
print(clientes_3)