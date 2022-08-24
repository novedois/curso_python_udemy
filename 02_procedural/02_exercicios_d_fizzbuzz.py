'''
Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se 
o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne
o número enviado.
'''

def fizz_buzz(numero):

    if numero % 3 == 0 and numero % 5 == 0:
        return 'Fizz Buzz'
    if numero % 3 == 0:
        return 'Fizz'
    if numero % 5 == 0:
        return 'Buzz'

    return numero

for i in range(31):
    print(fizz_buzz(i))