from random import randint

class Pessoa:
	ano_atual = 2022

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def get_ano_nascimento(self):
		print(self.ano_atual - self.idade)

	# Método de classe, relaciona-se a classe em si
	# Use se for relacionado a classe e não a uma instância
	@classmethod
	def por_ano_nascimento(cls, nome, ano_nascimento):
		idade = cls.ano_atual - ano_nascimento
		return cls(nome, idade)

	# Método estático
	@staticmethod
	def gera_id():
		rand = randint(10000, 19999)
		return rand

p1 = Pessoa('Filipe', 30)
p1.get_ano_nascimento()

p2 = Pessoa.por_ano_nascimento('João', 1990)
print(p2.nome)
print(p2.idade)
print(p2.gera_id())
# Roda pois é referente a classe etc
print(Pessoa.gera_id())
