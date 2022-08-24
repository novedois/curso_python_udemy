# Função decoradora
def master(funcao):
	def slave(*args, **kwargs):
		print('Estou decorada')
		funcao(*args, **kwargs)
	return slave

# Decorador
@master
def fala_oi():
	print('Oi')

@master
def outra_funcao(msg):
	print(msg)

variavel = fala_oi
variavel = master(fala_oi)
variavel()

outra_funcao('Olá eu sou Filipe')
