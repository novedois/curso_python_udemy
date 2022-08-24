'''
Crie uma função que exibe uma saudação com os parâmetros saudação e nome
'''

def saudacao(saudacao = 'Olá', nome = 'Usuário'):
    print(f'{saudacao}, {nome}')

print()

saudacao()
saudacao('Hello', 'My Guy')
saudacao(nome = 'Joãozinho\n')