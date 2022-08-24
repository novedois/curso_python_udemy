from dados import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)
nova_lista_comp = [ x * 2 for x in lista]

print(list(nova_lista))
print(nova_lista_comp)

for produto in produtos:
    print(produto)

# Acrescenta 5% ao valor de cada produto
def aumenta_preco(produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto

novos_produtos = map(aumenta_preco, produtos)

for preco in novos_produtos:
    print(preco)

# Faz alguma coisa com os nomes calmae
# Isso aqui não muda o dicionário em si, só copia os dados
# Para mudar, temos que fazer uma função
nomes = map(lambda p: p['nome'].upper(), pessoas)

for pessoa in nomes:
    print(pessoa)

# Função para mudar o dicionário
def nome_uppercase(pessoa):
    pessoa['nome'] = pessoa['nome'].upper()
    return pessoa

pessoas = map(nome_uppercase, pessoas)
print(list(pessoas))