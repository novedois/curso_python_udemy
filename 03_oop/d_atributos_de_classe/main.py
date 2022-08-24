class A:
	vc = 123

	def __init__(self):
		self.vc = 321

a1 = A()
a2 = A()

# A.vc = 321

a1.vc = 321

# QUando as intâncias são inicializadas (a1 e a2), o valor vira o do construtor
print(a1.vc)
print(a2.vc)

# O valor do vc da classe em si não é alterado pois não foi chamado o construtor
print(A.vc)

# print(a1.__dict__)
# print(a2.__dict__)
# print(A.__dict__)