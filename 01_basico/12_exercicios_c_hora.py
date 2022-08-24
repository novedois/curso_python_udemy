"""
-> Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
    descrito, exiba a saudação apropriada. Ex:
    Bom dia 0 - 11; Boa tarde 12 - 17; Boa noite 18 - 23
"""

try:
    hora = int(input("\nDigite a hora [0-23]: "))

    if hora >= 0 and hora <= 11:
        print("\nBom dia!\n")
    elif hora >= 12 and hora <= 17:
        print("\nBoa tarde!\n")
    elif hora >= 18 and hora <= 23:
        print("\nBoa noite!\n")
    else:
        print("\nHora inválida.\n")
except:
    print("\nNão foi digitado um número inteiro!\n")
    