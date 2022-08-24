from msilib.schema import Error
from multiprocessing.sharedctypes import Value


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise 

try:
    print(divide(2, 0))
except ZeroDivisionError as erro:
    print(erro)

def divide_2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser zero.')
    return n1 / n2

print(divide_2(5, 2))
try:
    print(divide_2(5, 0))
except ValueError as error:
    print(error)