# Variável com escopo global
variavel = 'valor'
variavel_mod = 'serei mudada'

def func():
    print(variavel)

def func_2():
    # Escopo local, só tem este valor dentro desta função
    # Não se pode mudar uma variável global de dentro de uma função assim
    # Mudar uma variável global a partir de uma função é considerado má prática
    variavel = 'outro_valor'
    
    # Edita o valor da variável global (NÃO É BOA PRÁTICA)
    global variavel_mod
    variavel_mod = 'fui mudada'

    print(variavel)
    print(variavel_mod)


func()
func_2()

print(variavel)
print(variavel_mod)

# Dá erro, usando a variável antes de setar
def func_3():
    print(variavel)
    variavel = 1234
    print(variavel)

# func_3()