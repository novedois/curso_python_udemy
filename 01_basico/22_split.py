string = 'O Brasil é o o o o país do futebol, o Brasil é penta'
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(f'\nlista_1: {lista_1}')
print(f'lista_2: {lista_2}\n')

# Imprime a segunda lista, tirando os espaços extras e capitalizando
for valor in lista_2:
    print(valor.strip().capitalize())

print()

# Conta quantas vezes cada palavra apareceu na frase
for valor in lista_1:
    print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}x na frase')

# Checa qual foi a palavra mais usada
palavra = ''
contagem = 0

for valor in lista_1:
    # Quantas vezes cada palavra apareceu
    qtd_vezes = lista_1.count(valor)

    # Se apareceu mais que o valor de contagem, mudamos a palavra e a quantidade
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'\nA palavra que apareceu mais vezes foi: {palavra}, {contagem}x\n')