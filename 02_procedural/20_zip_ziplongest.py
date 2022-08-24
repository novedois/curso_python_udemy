
estados = [ 'PE', 'SP', 'RJ' ]
cidades = [ 'Recife', 'São Paulo', 'Rio de Janeiro', 'Salvador ']

# zip retorna um iterador (o next funciona)
# Funciona apenas até a menor lista
cidades_estados = zip(cidades, estados)

for valor in cidades_estados:
    print(valor[0], valor[1])

from itertools import zip_longest, count

indice = count()
cidades_estados_2 = zip_longest(
    cidades, 
    estados, 
    fillvalue='Estado incerto'
)

# Se usássemos o índice com o zip_longest, 
# haveria um loop infinito
cidades_estados_3 = zip(
    indice,
    cidades,
    estados
)

for valor in cidades_estados_2:
    print(valor[0], valor[1])

for indice, cidade, estado in cidades_estados_3:
    print(indice, cidade, estado)