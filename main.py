import unittest
from PartidaTest import TestPartida

class test:
  TestPartida().testDefinirGols()
  TestPartida().testInstancePartida()

if __name__ == '__main__':
  unittest.main()

# import random  
# brasil = []
# argentina = []
# golsBrasil = 0
# golsArgentina = 0

# for i in range(1,91):
#   brasil.append(calcPartida())
#   argentina.append(calcPartida())

# def definirResult(a):
#   if a <= 0.4:
#     return "Estão na disputa pela a posse da Bola"

#   elif a > 0.4 and a <= 0.45:
#     return "Eles roubam a posse da bola"

#   elif a > 0.45 and a <= 0.5:
#     return "Eles partem pro ataque"

#   elif a > 0.5 and a <= 0.53:
#     return "Recuam a bola para defesa"

#   elif a > 0.53 and a <= 0.58:
#     return "Tocam a bola no meio"

#   elif a > 0.58 and a <= 0.62:
#     return "Parte para lateral do campo"

#   elif a > 0.62 and a <= 0.65:
#     return "Encara a marcação"

#   elif a > 0.65 and a <= 0.69:
#     return "Chamou pra dançar"

#   elif a > 0.69 and a <= 0.73:
#     return "Levou para a linha de fundo"

#   elif a > 0.73 and a <= 0.75:
#     return "Chutou pra fora"

#   elif a > 0.73 and a <= 0.75:
#     return "Chutou pro gol mas o goleiro defendeu, é só tiro de meta pro time adversario"

#   elif a > 0.76 and a <= 0.78:
#     return "Cruzou na area e tira o zagueiro"

#   elif a > 0.78 and a <= 0.79:
#     return "Invadiu a pequena area"

#   elif a > 0.79 and a <= 0.80:
#     return "Errou pegou mal na bola"

#   elif a > 0.81 and a <= 0.84:
#     return "fez a finta"

#   elif a > 0.84 and a <= 1:
#     return "GOOOOLL!"

#   return "E a bola saiu pela lateral"

# count = 0

# while count != 45:
  
#   if argentina[count] > brasil[count]:
#     argentinaT = definirResult(argentina[count])
#     if argentinaT == "GOOOOLL!":
#       golsArgentina += 1
#     print("ARGENTINA: " + argentinaT)

#   elif argentina[count] < brasil[count]:
#     brasilT = definirResult(brasil[count])
#     if brasilT == "GOOOOLL!":
#       golsBrasil += 1
#     print("BRASIL: " + brasilT)

#   elif argentina[count] == brasil[count]:
#     print("JUIZ: E o juiz chama atenção dos dois times!")
  
#   count += 1

# print("\n\n\n\n\ngols Argentina: " + str(golsArgentina))
# print("gols Brasil: " + str(golsBrasil))
# print( "\n\n\n\nFINAL DO PRIMEIRO TEMPO\n\n\n\n")

# while count != 90:
  
#   if argentina[count] > brasil[count]:
#     argentinaT = definirResult(argentina[count])
#     if argentinaT == "GOOOOLL!":
#       golsArgentina += 1
#     print("ARGENTINA: " + argentinaT)

#   elif argentina[count] < brasil[count]:
#     brasilT = definirResult(brasil[count])
#     if brasilT == "GOOOOLL!":
#       golsBrasil += 1
#     print("BRASIL: " + brasilT)

#   elif argentina[count] == brasil[count]:
#     print("JUIZ: E o juiz chama atenção dos dois times!")
  
#   count += 1

# print("\n\n\n\n\ngols Argentina: " + str(golsArgentina))
# print("gols Brasil: " + str(golsBrasil))
# print( "\n\n\n\nFINAL DA PARTIDA")