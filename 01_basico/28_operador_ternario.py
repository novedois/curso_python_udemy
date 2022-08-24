logged_user = True

if logged_user:
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar'


# Ternário

logged_user_2 = False
msg_2 = 'Usuário 2 Logado' if logged_user_2 else 'Usuário precisa logar.'

print(msg)
print(msg_2)

idade = int(input('Digite a sua idade: '))
eh_de_maior = idade >= 18

msg = 'Pode acessar' if eh_de_maior else 'Não pode acessar'
print(msg)


print('Pode entrar') if idade >= 18 else print('Não pode entrar')