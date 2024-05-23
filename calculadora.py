class calculadora:
    def __init__(self):
        pass
    def soma(self, num1, num2):
        return num1+ num2
    def subtracao(self, num1, num2):
        return num1-num2
    def multiplicacao(self, num1, num2):
        return num1*num2
    def divisao(self, num1, num2):
        if num2 != 0:
            return num1/num2
        else:
            return("nao pode ")
    def calcular (self):
        operacao = input('digite a operação(+,-,*,/):')
        num1 = float(input('digite o first number: '))
        num2 = float(input('digite o second number: '))
        if operacao == "+":
            resultado = self.soma(num1, num2)
        elif operacao == "-":
            resultado = self.subtracao(num1, num2)
        elif operacao == "*":      resultado = self.multiplicacao(num1, num2)
        elif operacao == "/":
            resultado = self.divisao(num1, num2)
        print("Seu resultado: ", resultado)
resultadocalc = calculadora()
resultadocalc.calcular()