"""
-> Faça um programa que peça ao usuário para digitar um número inteiro,
    informe se este número é par ou ímpar. Caso o usuário não digite um
    número inteiro, informe que não é um número inteiro.
"""

try:
    num = int(input("\nDigite um número: "))
    if num % 2 == 0:
        print(f"\n{num} par.\n")
    else:
        print(f"\n{num} ímpar.\n")
except:
    print("\nNão foi digitado um número inteiro.\n")