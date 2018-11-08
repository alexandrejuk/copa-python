import random

class Partida:
  def __init__(self, selecaoA, selecaoB):
    self.__selecaoA = selecaoA
    self.__statusSelecaoA = []
    self.__selecaoB = selecaoB
    self.__statusSelecaoB = []
    self.__vencedor = None
    self.__perdedor = None
    self.__golsSelecaoA = 0
    self.__golsSelecaoB = 0

  def __calcularPartida(self):
    return round((round(random.random(),2) * 0.87 ), 2)

  def criarPartida(self):
    for i in range(1,20):
      self.__statusSelecaoA.append(self.__calcularPartida())
      self.__statusSelecaoB.append(self.__calcularPartida())
  
  def __checarGol(self, a):
    if a > 0.84 and a <= 1:
      return 1
    return 0

  def definirGols(self):
    for i in range(len(self.__statusSelecaoA)):
      if self.__statusSelecaoA[i] > self.__statusSelecaoB[i]:
        self.__registrarGolsMarcadosA(self.__checarGol(self.__statusSelecaoA[i]))
      elif self.__statusSelecaoA[i] < self.__statusSelecaoB[i]:
        self.__registrarGolsMarcadosB(self.__checarGol(self.__statusSelecaoB[i]))

  def criarPenaltis(self):
    return 'partida criar'

  def __registrarGolsMarcadosA(self, gols):
    self.__golsSelecaoA += gols
    
  def __registrarGolsMarcadosB(self, gols):
    self.__golsSelecaoB += gols

  def registrarVencedor(self, selecao):
    self.__vencedor = selecao

  def registrarPerdedor(self, selecao):
    self.__perdedor = selecao

  def informarVencedor(self):
    return self.__vencedor
  
  def informarPerdedor(self):
    return self.__perdedor

  def informarGolsSelecaoA(self):
    return self.__golsSelecaoA
  
  def informarGolsSelecaoB(self):
    return self.__golsSelecaoB