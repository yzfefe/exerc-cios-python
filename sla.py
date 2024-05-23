import random

class MegaSena:

    def init(self, numeros):
        self.numeros_sorteados = []

    def gerar_numeros(self):
        self.numeros_sorteados = random.sample(range(1, 61), 6)
        self.numeros_sorteados.sort()

    def resultado(self):
        return self.numeros_sorteados

mega_sena = MegaSena()
mega_sena.gerar_numeros()
numeros_sorteados = mega_sena.resultado()

print("Os números que foram sorteados no jogo do bicho foram :", numeros_sorteados)