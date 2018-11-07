class Selecao():
  def __init__(
    self,
    nome,
    forcaAtaque,
    forcaDefesa,
    saldoDeGols,
    vitorias,
    derrotas,
    golsMarcados,
    golsSofridos,
    pontuacao
  ):
    self.__nome = nome
    self.__forcaAtaque = forcaAtaque
    self.__forcaDefesa = forcaDefesa
    self.__saldoDeGols = saldoDeGols
    self.__vitorias = vitorias
    self.__derrotas = derrotas
    self.__golsMarcados = golsMarcados
    self.__golsSofridos = golsSofridos
    self.__pontuacao = pontuacao

  def atualizarSelecao(self, Ataque, Defesa):
    self.__forcaAtaque = Ataque
    self.__forcaDefesa = Defesa

  def atualizarGolsMarcados(self, value):
    self.__golsMarcados += value
  
  def atualizarGolsSofridos(self, value):
    self.__golsSofridos += value

  def atualizarSaldoDeGols(self, value):
    self.__golsMarcados += value

  def atualizarVitorias(self, value):
    self.__vitorias += value

  def atualizarDerrotas(self, value):
    self.__derrotas += value

  def atualizarPontuacao(self, value):
    self.__pontuacao += value
