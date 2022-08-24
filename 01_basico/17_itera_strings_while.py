frase = 'o rato roeu a roupa do rei de roma' # iterável
tamanho_frase = len(frase)
nova_string = ''
input_usuario = input('\nQual letra deseja colocar maiúscula: ')

contador = 0

while contador < tamanho_frase:
    print(f'{frase[contador]} -> {contador}')
    
    letra = frase[contador]

    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra

    print(nova_string)
    contador += 1
else:
    print("\nAcabou o laço :3\n")

