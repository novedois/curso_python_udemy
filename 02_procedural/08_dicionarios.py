# Estrutura de dados que suporta uma chave e um valor
# Se as chaves tiverem o mesmo nome, só será mostrada a última
# Use chaves diferentes etc
# Geralmente se usam strings, mas as chaves podem ser de qualquer valor imutável


d1 = { 'chave': 'valor' }

# Adiciona uma chave e um valor
d1['nova_chave'] = 'Valor da nova chave'

print(f'\nPrimeiro dicionário: {d1}')
print(f'd1["chave"]: {d1["chave"]}')

# print(d1['valor']) - Dá erro

d2 = dict(
    chave_1 = 'Valor da primeira chave', 
    chave_2 = 'Valor da outra chave'
)

print(f'\nSegunda lista, antes da modificação: {d2}')

# Modifica o valor de uma chave
# 1ª forma
d2['chave_1'] = 'Fui modificada'
# 2ª forma
d2.update({'chave_2': 'Também fui modificada, que coisa'})

print(f'Segunda lista, depois da modificação: {d2}\n')

# Você pode usar uma tupla como chave (já que ela é imutável)
# Mas esta tupla deve ser composta apenas de valores imutáveis

d3 = {
    'str': 'valor',
    2: 'Outro valor',
    (1, 2, 3): 'Tupla'
}

print(f'\nUsando tupla como chave: {d3}')
print(f'd3[1, 2, 3]: {d3[1, 2, 3]}')

if 'chave_abuble' in d3:
    print('Existo :D')

d3['chave_abuble'] = 'Agora existo'

if 'chave_abuble' in d3:
    print('\nUma chave foi criada! :D\n')


# Usar o get não dá erro, não quebra a execução do programa
print('Get: ', d3.get('chave_oie'))

# Checa os valores (anteriormente estavamos checando as CHAVES)
# Pode usar keys e tal, mas não precisa
print('\nd3.values(): ', d3.values())
print('\n"Tupla" in d3.values(): "', 'Tupla' in d3.values())

# O len mostra quantos PARES existem no dicionário
print("len(d3): ", len(d3))

# Iterando por dicionários
d4 = {
    'chave_1': 'Primeiro valor',
    'chave_2': 'Segundo valor',
    'chave_3': 'Terceiro valor'
}

print('\nIterando sobre chaves:')
# Itera sobre as chaves (pode usar o keys, mas nõa precisa)
for key in d4:
    print(key)

print('\nIterando sobre valores')
# Itera sobre os valores
for valor in d4.values():
    print(valor)

print('\nIterando sobre itens (chaves e valores):')
# Itera sobre chaves e valores (gera tuplas)
for item in d4.items():
    print(item)

print('\nIterando sobre itens (chaves e valores):')
# Mesma coisa acima, mas com uma formatadinha etc
for item in d4.items():
    print(f'Chave: {item[0]} || Valor: {item[1]}')

print('\nIterando sobre itens (desempacotandos):')
# Também pode desempacotar
for chave, valor in d4.items():
    print(f'Chave: {chave} || Valor: {valor}')