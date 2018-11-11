class Selecao:
  def __init__(self, nome, fase):
    self.__nome = nome
    self.__gols = 0
    self.__vitorias = 0
    self.__fase = fase
    
  def getNome(self):
    return self.__nome

  def getGols(self):
    return self.__gols

  def getVitorias(self):
    return self.__vitorias

  def getFase(self):
    return self.__fase

  def updateFase(self, fase):
    self.__fase = fase
  
  def addGols(self, value):
    self.__gols += value
  
  def addVitoria(self, value):
    self.__vitorias += value