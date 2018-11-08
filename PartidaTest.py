import unittest
from Partida import Partida

instanciaPartida = Partida("Brazil", "Argentina")

class TestPartida(unittest.TestCase):

  def testDefinirGols(self):
    criarPartida = instanciaPartida.criarPartida()
    definirGols = instanciaPartida.definirGols()
    golsSelecaoA = instanciaPartida.informarGolsSelecaoA()
    golsSelecaoB = instanciaPartida.informarGolsSelecaoB()

  def testInstancePartida(self):
    self.assertIsInstance(instanciaPartida, Partida)
    