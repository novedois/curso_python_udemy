string = 'O Brasil é penta'
string_array = [ 'Meu', 'nome', 'é', 'Filipe', 'meua', 'migo' ]

lista = string.split(' ')

string_2 = ' '.join(lista)
string_3 = ' '.join(string_array)
string_4 = '*'.join(string_array)

print(f'''
Antes do join:

Primeira lista: {lista}
Segunda lista: {string_array}

Depois do join

Primeira frase...............: {string_2}
Segunda frase................: {string_3}
Terceira frase (* separando).: {string_4}
''')