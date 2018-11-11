import random
import algoritmoWin

class Partida:
  def __init__(self):
    self.__statusSelecaoA = []
    self.__statusSelecaoB = []

    self.__vencedor = None
    self.__perdedor = None

  def iniciar(self, timeA, timeB):
    for i in range(1):
      self.__statusSelecaoA.append(algoritmoWin.calcWin(random.uniform))
      self.__statusSelecaoB.append(algoritmoWin.calcWin(random.uniform))
    self.__calcPartida(timeA, timeB)
   
  def __calcPartida(self, timeA, timeB):
    for i in range(len(self.__statusSelecaoA)):
      if self.__statusSelecaoA[i] > self.__statusSelecaoB[i]:
        golA = self.__checarGol(self.__statusSelecaoA[i])
        timeA.addGols(golA)
      elif self.__statusSelecaoA[i] < self.__statusSelecaoB[i]:
        golB = self.__checarGol(self.__statusSelecaoB[i])
        timeB.addGols(golB)

    if timeA.getGols() > timeB.getGols():
      self.__vencedor = timeA.getNome()
      timeA.addVitoria(1)
    else:
      self.__perdedor = timeB.getNome()
      timeB.addVitoria(1)

  def __checarGol(self, a):
    if a == 0.85:
      return 1
    return 0