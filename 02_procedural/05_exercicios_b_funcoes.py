'''
Crie uma função_1 que recebe uma funcao_2 como parâmetro e retorna o valor da
funcao_2 executada. Faça a funcao_1 executar duas funções que recebam um número
diferente de argumentos
'''

def super_func(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_opa(nome):
    return f'Opa {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'

print(super_func(fala_opa, 'Filipe'))
print(super_func(saudacao, 'Filipe', saudacao='Boa tarde'))