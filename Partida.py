import random
import algoritmoWin

class Partida:
  def __init__(self, selecaoA, selecaoB):
    self.__selecaoA = selecaoA
    self.__golsSelecaoA = 0
    self.__statusSelecaoA = []

    self.__selecaoB = selecaoB
    self.__golsSelecaoB = 0
    self.__statusSelecaoB = []

    self.__vencedor = None
    self.__perdedor = None



  def iniciarPartida(self):

    for i in range(1,91):
      self.__statusSelecaoA.append(algoritmoWin.calcWin(random.random, self.__selecaoA.getAtk()))
      self.__statusSelecaoB.append(algoritmoWin.calcWin(random.random, self.__selecaoB.getAtk()))

    self.__calcularGols()
    
    self.__selecaoA.putGols(self.__golsSelecaoA)
    self.__selecaoB.putGols(self.__golsSelecaoB)

    if self.__golsSelecaoA == self.__golsSelecaoB: 
      
      if self.__selecaoA.getGols() > self.__selecaoB.getGols():
        self.__vencedor = self.__selecaoA.getNome()
        self.__perdedor = self.__selecaoB.getNome()
        self.__selecaoA.putVitoria(1)

      else:
        self.__vencedor = self.__selecaoB.getNome()
        self.__perdedor = self.__selecaoA.getNome()
        self.__selecaoB.putVitoria(1)

    elif self.__golsSelecaoA > self.__golsSelecaoB:
      self.__vencedor = self.__selecaoA.getNome()
      self.__perdedor = self.__selecaoB.getNome()
      self.__selecaoA.putVitoria(1)

    else:
      self.__vencedor = self.__selecaoB.getNome()
      self.__perdedor = self.__selecaoA.getNome()
      self.__selecaoB.putVitoria(1)
  

  def __calcularGols(self):

    for i in range(len(self.__statusSelecaoA)):

      if self.__statusSelecaoA[i] > self.__statusSelecaoB[i]:
        self.__golsSelecaoA += self.__checarGol(self.__statusSelecaoA[i])

      elif self.__statusSelecaoA[i] < self.__statusSelecaoB[i]:
        self.__golsSelecaoB += self.__checarGol(self.__statusSelecaoB[i])
    
  def __checarGol(self, a):
    if a > 0.84 and a <= 1:
      return 1
    return 0

  def vencedor(self):
    return self.__vencedor 

  def perdedor(self):
    return self.__perdedor