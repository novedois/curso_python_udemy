usuario = input("\nNome do usuário: ")
senha = input("Senha do usuário: ")

usuario_bd = "luiz"
senha_bd = "123456"

if usuario_bd == usuario and senha_bd == senha:
    print("Você está logado no sistema!\n")
else:
    print("Usuário ou senha inválidos\n")

print("a" in "Filipe")
print("a" not in "Filipe")

num = int(input("Digite um número: "))

if num == 3 or num == 7:
    print("Este é um dos números da sorte!")
else:
    print("Que azar, poxa")

print()


