class Partida:
  def __init__(self, selecaoA, selecaoB):
    self.__selecaoA = selecaoA
    self.__selecaoB = selecaoB
    self.__vencedor = None
    self.__perdedor = None
    self.__golsSelecaoA = 0
    self.__golsSelecaoB = 0

  def criarPartida(self):
    return 'partida criar'
  
  def criarPenaltis(self):
    return 'partida criar'

  def registrarGolsMarcadosA(self, gols):
    self.__golsSelecaoA += gols
    
  def registrarGolsMarcadosB(self, gols):
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