import random
import selecoesData

from Partida import Partida
from Selecao import Selecao
from Torneio import Torneio

jogo = Partida()
selecoes = selecoesData.selecoes()
qtdSelecoes = len(selecoes)
torneio = Torneio()
count = 0
grupo = []

for i in range(40):
  letraGrupo = chr(65 + count) 
  selecao = Selecao(selecoes[random.randrange(0, qtdSelecoes)], letraGrupo)

  if len(grupo) == 0:
    grupo.append(selecao)

  elif len(grupo) < 4:
    grupo.append(selecao)

  elif len(grupo) == 4:
    torneio.registrarGrupo(grupo)

    grupo = []
    count += 1

grupos = torneio.informarGrupos()

for g in range(len(grupos)):
  for i in range(4):
    for j in range(3):
      if i == 0 or i == 1 and j!= 0 and j != 1 or i == 2 and j != 1 and j != 3:
        timeA = grupos[g][i]
        timeB = grupos[g][j+1]
        jogo.iniciar(timeA, timeB)

classificados = []
count = 0

for i in range(len(grupos)):
  for j in range(len(grupos[j])):
    if count != 8:
      if len(classificados) == 0:
        if grupos[i][j].getVitorias() == 1 :
          classificados.append(grupos[i][j])
      if len(classificados) < 2:
        if grupos[i][j].getVitorias() > 1:
          classificados.append(grupos[i][j])
      if len(classificados) == 2:
        torneio.registrarOitavas(classificados)
        classificados = []
        count += 1


oitavasFinais = torneio.informarOitavas()

for i in range(len(oitavasFinais)):
  jogo.iniciar(oitavasFinais[i][0], oitavasFinais[i][1])


classificadosQuarta = []
count4 = 0

for i in range(len(oitavasFinais)):
  if count4 != 4:
    if len(classificadosQuarta) == 0:
      if oitavasFinais[i][0].getVitorias() > oitavasFinais[i][1].getVitorias():
        classificadosQuarta.append(oitavasFinais[i][0])
    
    if len(classificadosQuarta) < 2:
      if oitavasFinais[i][0].getVitorias() > oitavasFinais[i][1].getVitorias():
        classificadosQuarta.append(oitavasFinais[i][0])

      if oitavasFinais[i][0].getVitorias() < oitavasFinais[i][1].getVitorias():
        classificadosQuarta.append(oitavasFinais[i][1])
      
      if oitavasFinais[i][0].getVitorias() == oitavasFinais[i][1].getVitorias():
        if oitavasFinais[i][0].getGols() > oitavasFinais[i][1].getGols():
          classificadosQuarta.append(oitavasFinais[i][0])

        if oitavasFinais[i][0].getGols() < oitavasFinais[i][1].getGols():
          classificadosQuarta.append(oitavasFinais[i][1])
        
        if oitavasFinais[i][0].getGols() == oitavasFinais[i][1].getGols():
          classificadosQuarta.append(oitavasFinais[i][0])
    if len(classificadosQuarta) == 2:
      torneio.registrarQuartas(classificadosQuarta)
      classificadosQuarta = []
      count4 += 1

quartasFinais = torneio.informarQuartas()

for i in range(len(quartasFinais)):
  jogo.iniciar(quartasFinais[i][0], quartasFinais[i][1])

classificadosSemifinal = []
countSemi = 0

for i in range(len(quartasFinais)):
  if countSemi != 2:
    if len(classificadosSemifinal) == 0:
      if quartasFinais[i][0].getVitorias() > quartasFinais[i][1].getVitorias():
        classificadosSemifinal.append((quartasFinais[i][0]))
      
    if len(classificadosSemifinal) < 2:
      if quartasFinais[i][0].getVitorias() > quartasFinais[i][1].getVitorias():
        classificadosSemifinal.append((quartasFinais[i][0]))
      
      if quartasFinais[i][0].getVitorias() < quartasFinais[i][1].getVitorias():
        classificadosSemifinal.append((quartasFinais[i][1]))

      if quartasFinais[i][0].getVitorias() == quartasFinais[i][1].getVitorias():
        if quartasFinais[i][0].getGols() > quartasFinais[i][1].getGols():
          classificadosSemifinal.append((quartasFinais[i][0]))
        else:
          classificadosSemifinal.append((quartasFinais[i][1]))
    if len(classificadosSemifinal) == 2:
      torneio.registrarSemifinal(classificadosSemifinal)
      classificadosSemifinal = []
      countSemi += 1      

semifinal = torneio.informarSemifinal()

for i in range(len(semifinal)):
  jogo.iniciar(semifinal[i][0], semifinal[i][1])

classificadosFinal = []
terceiroLugar = []
countFinal = 0

for i in range(len(semifinal)):
  if semifinal[i][0].getVitorias() > semifinal[i][1].getVitorias():
    classificadosFinal.append(semifinal[i][0])
  if semifinal[i][0].getVitorias() < semifinal[i][1].getVitorias():
    classificadosFinal.append(semifinal[i][1])
    
  if semifinal[i][0].getVitorias() == semifinal[i][1].getVitorias():
    if semifinal[i][0].getGols() > semifinal[i][1].getGols():
      classificadosFinal.append(semifinal[i][0])
    else:
      classificadosFinal.append(semifinal[i][1])

torneio.registrarFinal(classificadosFinal)
final = torneio.informarFinal()
jogo.iniciar(final[0][0], final[0][1])

if final[0][0].getGols() > final[0][1].getGols():
  print('1 Lugar na copa para a selecao ', final[0][0].getNome(), ' gols: ', final[0][0].getGols())
  print('2 Lugar na copa para a selecao ', final[0][1].getNome(), ' gols: ', final[0][1].getGols())
else:
  print('1 Lugar na copa para a selecao ', final[0][1].getNome(), ' gols: ', final[0][1].getGols())
  print('2 Lugar na copa para a selecao ', final[0][0].getNome(), ' gols: ', final[0][0].getGols())
  
