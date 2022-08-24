nome = 'Filipe'
qtd_caracteres = len(nome)

if qtd_caracteres < 6:
    print('\nVocê precisa digitar pelo menos 6 caracteres\n')
else:
    print('\nCadastrado com sucesso\n')

str_1 = input("Digite alguma coisa: ")
str_2 = input("Digite outra coisa: ")

print(f'A quantidade de caracteres digitados foi: {len(str_1) + len(str_2)}\n')