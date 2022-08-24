nome = 'Filipe'
idade = 20
salario = 2500.24

print(f"\nSeu nome é {nome}, você tem {idade} anos e seu salário é de R${salario:.2f}")
print("Seu nome é {}, você tem {} anos e seu salário é de R${:.2f}".format(nome, idade, salario))
print("Seu nome é {n}, você tem {i} anos e seu salário é de R${s:.2f}".format(n=nome, i=idade, s=salario))
print("Seu nome é {2}, você tem {0} anos e seu salário é de R${1}\n".format(nome, idade, salario))