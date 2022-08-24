'''
Módulos padrão do Python
-> São arquivos .py e servem para expandir as 
   funcionalidades padrão da linguagem

'''

# import sys
from sys import platform as so
from random import randint as ri

# print(sys.platform)
# print(platform)
print(so)

for i in range(10):
	# print(random.randint(0, 10))
	# print(randint(0, 10))
	print(ri(0, 10))