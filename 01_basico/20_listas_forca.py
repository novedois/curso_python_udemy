secreto = 'perfume'
digitadas = []

tentativas = 1

print('\n* * * * Forca * * * *\n')

while True:
    if tentativas > 5:
        print('\nVocê perdeu :/')
        print('\nFim do programa\n')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Não vale! Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Yes! {letra} existe na palavra secreta\n')
    else:
        print(f'Puts, {letra} não existe na palavra secreta :/\n')
        digitadas.pop()
    
    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secreto:
        print('\n* * * Você ganhou! :D * * *\n')
        print(f'Palavra secreta: {secreto}')
        print('\nFim do programa\n')
        break
    else:
        print(secreto_temporario)
    
    if letra not in secreto:
        tentativas += 1
    
    print(f'{tentativas - 1}/5 tentativas.\n')