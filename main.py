import random
import selecoesData

from Selecao import Selecao
from Torneio import Torneio
from Partida import Partida

selecoes = selecoesData.selecoes()
qtdSelecoes = len(selecoes)
torneio = Torneio()

count = 0
grupo = []

for i in range(40):
  letraGrupo = chr(65 + count) 
  selecao = Selecao(selecoes[random.randrange(0, qtdSelecoes)], 0, 0, "grupo " + letraGrupo, 0.84)

  if len(grupo) == 0:
    grupo.append(selecao)

  elif len(grupo) < 4:
    grupo.append(selecao)

  elif len(grupo) == 4:
    torneio.registrarGrupo(grupo)

    grupo = []
    count += 1

iSel = torneio.informarGrupos()
for i in range(len(iSel)):
 for j in range(4):
   print(iSel[i][j].getFase() +': '+iSel[i][j].getNome())



# selecaoA = Selecao("Brasil", 0, 0, "grupo A", 0.84)
# selecaoB = Selecao("Argentina", 0, 0, "grupo A", 0.85)
# grupo = [selecaoA, selecaoB]

# partida = Partida(grupo[0], grupo[1])
# iniciar = partida.iniciarPartida()

# v = str(selecaoA.getGols())
# p = str(selecaoB.getGols())

# print('Gols A ==============>>> ', selecaoA.getNome(), v)
# print('Gols B ==============>>> ', selecaoB.getNome(), p)
