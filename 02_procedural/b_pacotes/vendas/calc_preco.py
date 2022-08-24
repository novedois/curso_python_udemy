from vendas.formata import preco

def aumento(valor, porcentagem, formata = False):
	r = valor + (valor * (porcentagem / 100))
	if formata:
		return preco.real(r)
	return r

def reducao(valor, porcentagem, formata = False):
	r = valor - (valor * (porcentagem / 100))
	if formata:
		return preco.real(r)
	return r