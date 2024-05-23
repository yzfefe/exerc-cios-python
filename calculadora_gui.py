import tkinter as tk
import math

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("800x600")

rotulo1 = tk.Label(janela, text="Informe o primeiro número")
rotulo1.pack()

entrada_num1 = tk.Entry(janela)
entrada_num1.pack(padx=10, pady=10)


rotulo2 = tk.Label(janela, text="Informe o segundo número")
rotulo2.pack()

entrada_num2 = tk.Entry(janela)
entrada_num2.pack(padx=10, pady=10)

opcao = tk.IntVar()
rb_soma = tk.Radiobutton(janela, text="+", variable=opcao, value=1)
rb_soma.pack()
rb_subtrai = tk.Radiobutton(janela, text="-", variable=opcao, value=2)
rb_subtrai.pack()
rb_multiplica = tk.Radiobutton(janela, text="*", variable=opcao, value=3)
rb_multiplica.pack()
rb_dividir = tk.Radiobutton(janela, text="/", variable=opcao, value=4)
rb_dividir.pack()
rb_potencia = tk.Radiobutton(janela, text="**", variable=opcao, value=5)
rb_potencia.pack()
rb_raiz = tk.Radiobutton(janela, text="raiz quadrada", variable=opcao, value=6)
rb_raiz.pack()

def calcular():
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    operacao = opcao.get()

    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 5:
        resultado = num1**num2
    elif operacao == 6:
        resultado = math.sqrt(num1)
    elif operacao == 4:
        if num2 == 0:
            resultado = "Erro, impossivel dividir por 0"
        else:
            resultado = num1 / num2
    else:
        resultado = "Erro, operação invalida"

    print(resultado)
    exibir.config(text= resultado)



botao = tk.Button(janela, text="Calcular", width=15, bg='pink', fg="navy", command=calcular)
botao.pack()

exibir = tk.Label(janela, text="sera exibido aqui")
exibir.pack()

janela.mainloop()