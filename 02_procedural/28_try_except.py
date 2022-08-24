# Assim é muito genérica, má prática
try:
    print(a)
except:
    print('Erro')

print("O código continua...\n")

# 000------------------------ #
# tratando a exceção

try:
    print(a)
except NameError as erro:
    print(f'Erro do desenvolvedor!: {erro}')

print("O código continua...\n")

# --------------------------- #

try:
    print(9 / 0)
except Exception as erro:
    print(f'Erro inesperado: {erro}')

print('O código continua...\n')

# --------------------------- # 
try:
    a = []
    print(a[2])
except IndexError as erro:
    print('Erro de índice')

print('O código continua...\n')

# --------------------------- # 
# Também dá pra fazer assim ó
# O else ocorre se o código não cair em nenhum erro
# Já o finally roda independente de erro ou não
try:
    a = {}
    print(a[1])
except NameError as erro:
    print(f'Erro do desenvolvedor: {erro}')
except (IndexError, KeyError) as erro:
    print(f'Erro de índice: {erro}')
except Exception as erro:
    print(f'Erro inesperado: {erro}')
else:
    print('Seu código foi executado')
finally:
    print('Finalmente! O código continua...\n')
    # Isso trata o erro... era esperado um a, devolvemos um a
    a = 'Opa'

print(a, '\n')

# --------------------------- # 