'''
Crie uma função que recebe 2 números. O primeiro é um valor e o segundo um
percentual (ex, 10%). Retorne (return) o valor do primeiro número somado com
o aumento percentual do mesmo.
'''

def soma_porcentagem(numero, porcentagem):
    valor_pct = (porcentagem / 100) * numero
    return numero + valor_pct

print()

print(soma_porcentagem(100, 10))
print(soma_porcentagem(200, 40))
print(soma_porcentagem(99, 3))

print()