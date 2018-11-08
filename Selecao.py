class Selecao:
  def __init__(self, nome, gols, vitoria, fase, atk):
    self.__nome = nome
    self.__gols = gols
    self.__vitoria = vitoria
    self.__fase = fase
    self.__atk = atk

  def getNome(self):
    return self.__nome
  
  def getFase(self):
    return self.__fase

  def addVitoria(self, value):
    self.__vitoria += value

  def addGols(self, value):
    self.__gols += value

  def getGols(self):
    return self.__gols

  def getAtk(self):
    return self.__atk