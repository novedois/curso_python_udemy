'''
Crie uma funcao_1 que recebe uma funcao_2 como parâmetro e retorne o valor 
da funcao_2 executada.
'''

def ola_mundo():
    return 'Olá mundo'

def super_func(funcao):
    return funcao()

print(super_func(ola_mundo))