num_1 = input("\nDigite um número: ")
num_2 = input("Digite um número: ")

try:
    num_1 = float(num_1)
    num_2 = float(num_2)

    print(num_1 + num_2)
except:
    print("\nError\n")