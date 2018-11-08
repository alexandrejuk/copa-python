class Torneio:
  def __init__(self):
    self.__faseGrupos = []

  def registrarGroupo(self, grupo):
    self.__faseGrupos.append(grupo)
    
  def informarGroupos(self):
    return self.__faseGrupos
