# SETTER -> configurando um valor (=)
# 			precisa ter um getter primeiro

# GETTER -> Obtem um valor (.)

class Pessoa:
	def __init__(self):
		self._nome = 'Inicial'

	@property
	def nome(self):
		return self._nome
	
	@nome.setter
	def nome(self, nome):
		nome += ' sei lá'
		self._nome = nome

	@property
	def sobrenome(self):
		return "Desconhecido"
	

p1 = Pessoa()
p1.nome = 'João'

print(p1.nome)
print(p1.sobrenome)
