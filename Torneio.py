class Torneio:
  def __init__(self):
    self.__faseGrupos = []
    self.__oitavas = []
    self.__quartas = []
    self.__semifinal = []
    self.__final = []

  def registrarGrupo(self, grupo):
    self.__faseGrupos.append(grupo)
    
  def informarGrupos(self):
    return self.__faseGrupos


  def registrarOitavas(self, grupos):
    self.__oitavas.append(grupos)


  def informarOitavas(self):
    return self.__oitavas

  def registrarQuartas(self, grupos):
    self.__quartas.append(grupos)

  def informarQuartas(self):
    return self.__quartas

  def registrarSemifinal(self, grupos):
    self.__semifinal.append(grupos)

  def informarSemifinal(self):
    return self.__semifinal

  def registrarFinal(self, grupo):
    self.__final.append(grupo)

  def informarFinal(self):
    return self.__final