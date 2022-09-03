from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
print(maquina)

caneta.escrever()
maquina.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

del escritor

print(caneta.marca)
maquina.escrever()