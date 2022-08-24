import time

cpf = '168.995.350-09'

print(f'\nCPF: {cpf}\n')

print('Fazendo separações...')

time.sleep(.5)

traco_separado = cpf.split('-')
primeiro_valor, ultimo_valor = traco_separado[0], traco_separado[1]
lista_numeros = list(''.join(primeiro_valor.split('.')))
lista_numeros_2 = list(''.join(primeiro_valor.split('.')))


print("\n... Calculando dígito 01!")
time.sleep(.5)

i = 0
j = 10
soma = 0
while j >= 2:
    num = int(lista_numeros[i])
    soma += num * j 
    i += 1
    j -= 1

resultado = 11 - (soma % 11)
digito_1 = 0

if resultado > 9:
    digito_1 = 0
else:
    digito_1 = resultado

print(f"Calculado! Dígito 01: {digito_1}")
print("\n... Calculando dígito 02!")
time.sleep(.5)

k = 0
l = 11
soma_2 = 0

lista_numeros.append(digito_1)

while l >= 2:
    num = int(lista_numeros[k])
    soma_2 += num * l 
    k += 1
    l -= 1

digito_2 = 11 - (soma_2 % 11)

print(f"Calculado! Dígito 02: {digito_2}\n")
time.sleep(.5)  

cpf_novo_lista = lista_numeros_2
cpf_novo_lista.append(str(digito_1))
cpf_novo_lista.append(str(digito_2))
novo_cpf_unido = ''.join(cpf_novo_lista)

cpf_original = primeiro_valor + ultimo_valor
cpf_original_unido = ''.join(cpf_original.split('.'))

print('Verificações finais....')
time.sleep(1)

if novo_cpf_unido == cpf_original_unido:
    print('\nCPF válido.\n')
else:
    print('\nCPF inválido\n')