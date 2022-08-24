nome = input("\nDigite o seu nome: ")
idade = int(input("Digite a sua idade: "))

idade_minima = 20
idade_maxima = 30

if idade >= idade_minima and idade <= idade_maxima:
    print(f"\n{nome} pode pegar o empréstimo\n")
else:
    print(f"\n{nome} não pode pegar o empréstimo\n")


