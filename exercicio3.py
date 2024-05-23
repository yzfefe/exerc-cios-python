class Calculadora:

    def __init__(self):
        pass
    def soma(self, num1, num2):
        return num1+num2
    
    def subtracao(self, num1, num2):
        return num1-num2
    
    def multiplicacao(self, num1, num2):
        return num1*num2
    
    def divisao(self, num1, num2):
        if num2 != 0:
            return num1/num2
        else: 
            return("n é possivel dividir por 0") 

minhacalculadora = Calculadora()
resultado = minhacalculadora.soma(20,29)
resultado2 = minhacalculadora.subtracao(20,29)
resultado3 = minhacalculadora.multiplicacao(20,29)
resultado4 = minhacalculadora.divisao(20,29)

print ("soma", resultado)
print ("subtração", resultado2)
print ("divisão", resultado4)
print ("multiplicação", resultado3)
