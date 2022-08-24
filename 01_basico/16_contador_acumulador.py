print()

contador = 0
acumulador = 0

while contador < 5:
    num = int(input("Digite um número: "))
    acumulador += num
    contador += 1

print(f"Contador: {contador}\nAcumulador: {acumulador}\n")

contador = 1
acumulador = 1

print()

while contador <= 10:
    print(contador, acumulador)
    acumulador += contador
    if acumulador > 10:
        break
    contador += 1
# Só será executado quando a expressão do laço for falsa (quando o laço for completo)
else:
    print("Laço completo.")

print("Você está lendo isso independente do laço :3")