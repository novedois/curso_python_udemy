clientes = {
    'cliente_1': {
        'nome': 'Filipe',
        'sobrenome': 'Azoubel'
    },
    'cliente_2': {
        'nome': 'João',
        'sobrenome': 'da Silva'
    },
    'cliente_3': {
        'nome': 'Ana',
        'sobrenome': 'Maria'
    }
}

for clientes_chaves, clientes_valores in clientes.items():
    print(f'Chaves: {clientes_chaves}')
    print(f'Valores: {clientes_valores}')


for clientes_chaves, clientes_valores in clientes.items():
    print(f'Exibindo: {clientes_chaves}')
    # Um loop para cada dicionário dentro do dicionário pai
    for dados_chaves, dados_valores in clientes_valores.items():
        print(f'\t{dados_chaves}: {dados_valores}')

# Ao atribuir um dicionário criado a uma variável, os dois irão ocupar
# o mesmo lugar na memória. São considerados o mesmo objeto. Por isso,
# se um for modificado, o outro também será

d1 = { 1: 'a', 2: 'b', 3: 'c' }
copia = d1

print(f'\nd1:\t {d1}')
print(f'Cópia:\t {copia}')

copia[1] = 'Fui modificado'

print(d1)
print(copia)
print(d1 == copia)

# Faz uma cópia raza
copia_2 = d1.copy()

copia_2[1] = 'Modificadíssima'

print(d1)
print(copia_2)

# Cuidado: Se houver uma lista no dicionário, o valor seria modificado em ambos
d2 = { 1: 'a', 2: 'b', 3: 'c', 4: ['Filipe', 'Azoubel'] }
copia_3 = d2.copy()

copia_3[4][0] = 'AAAA'

print(d2)
print(copia_3)

# Para copiar uma lista de verdade, deve-se importar um módulo 
# Mais sobre isso no futuro

# _------------------------------ #

# Cast para dicionário
# Pode ser com tuplas também etc
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
]

dict_lista = dict(lista)

print(dict_lista)

# Excluino arquivos
# Pop - precisa especificar qual chave será excluída
# Popitem - o último item será excluído 

dict_lista.pop('c1')
dict_lista.popitem()

print(dict_lista)

d3 = { 'chave_1': 'valor_1', 'chave_2': 'valor_2' }
d4 = { 'chave_A': 'valor_A', 'chave_B': 'valor_B' }

# Concatena dicionários
d3.update(d4)

print(d3)