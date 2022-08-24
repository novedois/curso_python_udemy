from re import X


x = 10
y = 'Luiz'
z = 'Filipe'

print(f'''
Antes de trocar:
x = {x}
y = {y}
z = {z}''')

x, y , z= z, x, y

print(f'''
Depois de trocar

x = {x}
y = {y}
z = {z}
''')