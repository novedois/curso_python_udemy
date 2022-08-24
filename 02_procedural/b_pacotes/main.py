# import vendas.calc_preco
# from vendas import calc_preco
from vendas.calc_preco import aumento, reducao
from vendas.formata import preco as pr

preco = 49.90

# preco_com_aumento = vendas.calc_preco.aumento(preco, 15)
# preco_com_aumento = calc_preco.aumento(preco, 15)
preco_com_aumento = aumento(preco, 15)
preco_com_reducao = reducao(preco, 15, True)

print(pr.real(preco_com_aumento))
print(preco_com_reducao)

