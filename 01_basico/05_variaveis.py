"""
- iniciar com letra
- pode conter numeros
- separar com _
- letras maiúsculas
"""

nome = 'Filipe Azoubel'     # str
idade = 29                  # int
altura = 1.73               # float
peso = 125.1                # float
eh_maior = idade > 18       # bool
imc = peso / altura ** 2    # float

print()

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', eh_maior)
print('IMC: ', imc)

print()

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

print()