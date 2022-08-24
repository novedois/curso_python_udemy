print()

x = 0

while x <= 100:
    if(x % 2 != 0):
        x += 1
        continue
    if x == 38:
        break
    print(x, end=" ")
    x += 1

print("\nAcabou!\n")

x = 0 # coluna
y = 0 # linha

while x < 10:
    y = 0
    while y < 5:
        print(f'x = {x} e y = {y}')
        y += 1
    x += 1

print("\nAcabou!\n")

print("Calculadora\n\n")

while True:
    
    num_1 = input("\nDigite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar um número.")
        continue
    
    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == "+":
        print(num_1 + num_2)
    elif operador == "-":
        print(num_1 - num_2)
    elif operador == "*":
        print(num_1 * num_2)
    elif operador == "/":
        print(num_1 / num_2)
    else:
        print("\nDigite um operador válido.\n")

    escolha = int(input("Digite 0 para sair: "))
    if escolha == 0:
        print("\n* * Fim do Programa * *")
        break