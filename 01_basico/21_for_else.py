
lista = [ 'Filipe', 'Maria', 'Vitória', 'Carlos' ]

print()

comeca_com_Fil = False

for nome in lista:
    print(f'Nome: {nome}')
    if nome.startswith('Fil'):
        comeca_com_Fil = True
        print('Filipe?? :D')
else:
    print("\nLaço terminado.")

if comeca_com_Fil:
    print('\nTem um Fil aí, serasse sou eu\n')
else:
    print('\nNo Fil oh no\n')