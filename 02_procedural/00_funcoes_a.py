def imprime(texto = 'String vazia!'):
    print(texto)

def saudacao(msg = 'Olá', nome = 'Usuário'):
    # Quantos comandos quiser
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)

imprime('Oie')
imprime()

saudacao('Olá', 'Filipe')
saudacao(nome = 'Leopoldo')
saudacao(nome = 'Mark', msg = 'Oh hi')
saudacao()
