# Depois que um argumento é nomeado, todos os que vem após precisam ser nomeados

def func(a1, a2, a3, a4, a5, nome = None, a6 = None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var = func(1, 2, 3, 4, 5, 'Luiz', '5')
print(var[0], var[1])

# Lembrando o asterisco
lista = [ 1, 2, 3, 4, 5 ]
n1, n2, *n = lista

print(n1, n2 , n)               # O n imprime o restante da lista 
print(*lista, sep='.')          # Desempacota a lista

# Quando não sei quantos argumentos, uso *args
def imprime(*args):
    print(args)

imprime('Olá', 'meu', 'amigo', 'Filipe')

# Os args são retornados me uma tupla (não pode ser modificada)
# Mas é possível fazer um cast para list
def func(*args):
    args = list(args)           # Transforma em lista para poder modificar
    args[1] = 'Opa'             # Modifica um valor qualquer
    print(args)                 # Imprime todos os elementos
    print(args[0])              # Imprime o primeiro argumento
    print(args[-1])             # Imprime o último argumento
    print(len(args))            # Imprime a quantidade de args
    

func(1, 2, 3, 4, 5)

def func_2(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
lista_2 = [ 10, 20, 30, 40, 50 ]

# Assim, fica um array dentro de uma tupla
func_2(lista)

# Desempacota as listas, integrando tudo (são mescladas)
func_2(*lista, *lista_2)

# Kwargs são argumentos com palavras chave (Keyword arguments)
def func_3(*args, **kwargs):
    print(args)                 # Tupla
    print(kwargs)               # Objeto (Dicionário?)

    # O get ajuda a evitar erros
    nome = kwargs.get('nome')
    idade = kwargs.get('idade')

    if nome is not None:
        print('Nome: ', nome)
    if idade is not None:
        print('Idade: ', idade)


func_3(*lista, *lista_2, nome = 'João', idade = 30)
