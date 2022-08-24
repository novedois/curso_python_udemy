from pessoa import Pessoa

p1 = Pessoa('Filipe', 30)
p2 = Pessoa('João', 32, False, True)

print(p1.nome)
print(p1.idade)
print(p1.comendo)
print(p1.falando)

p1.comer('Maçã')
p1.comer('Maçã')

print(p1.comendo)

p1.parar_comer()
p1.parar_comer()
p1.falar('Goiás')
print(p1.comendo)
p1.comer('Uva')
p1.parar_comer()

p1.falar('Goiás')
p1.parar_falar()
p1.falar('Fiat 147')

print(p1.ano_atual)
print(p2.ano_atual)

print(p1.get_ano_nascimento())