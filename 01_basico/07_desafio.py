"""
-> Criar variáveis para nome, idade, altura e peso de uma pessoa
-> Criar variável com o ano atual
-> Obter o ano de nascimento da pessoa (ano atual - idade)
-> Obter o IMC da pessoa com 2 casas decimais
-> Exibir um texto com todos os valores na tela usando F-strings
"""

nome = 'João da silva'
idade = 25
altura = 1.75
peso = 90
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'\n{nome} tem {idade} anos, {altura:.1f}m de altura e pesa {peso}kg')
print(f'O IMC de {nome} é de {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}\n')