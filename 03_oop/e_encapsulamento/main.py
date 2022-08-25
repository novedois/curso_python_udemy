
"""
_ 	protected (mais fraco)
__ 	privado (mais forte)
"""

class BaseDeDados:
	def __init__(self):
		self.__dados = {}

	@property
	def dados(self):
		return self.__dados
	

	def inserir_cliente(self, id, nome):
		if 'clientes' not in self.__dados:
			self.__dados['clientes'] = { id: nome }
		else:
			self.__dados['clientes'].update({id: nome})

	def lista_clientes(self):
		for id, nome in self.__dados['clientes'].items():
			print(id, nome)

	def apaga_cliente(self, id):
		del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Filipe')
bd.inserir_cliente(2, 'Maria')
bd.inserir_cliente(3, 'João')
bd.apaga_cliente(3)

bd.lista_clientes()

bd.__dados = "Não tenho acesso etc, sou adicionado pelo Python"

print(bd.__dados)
print(bd.dados)
# bd.lista_clientes()