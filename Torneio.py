class Torneio:
  def __init__(self):
    self.__faseGrupos = []

  def registrarGrupo(self, grupo):
    self.__faseGrupos.append(grupo)
    
  def informarGrupos(self):
    return self.__faseGrupos
