import tkinter as tk

janela = tk.Tk()
janela.title ("GUI")
janela.geometry("800x600")

rotulo= tk.Label (janela, text= "interface")
rotulo.pack()

def clique():
    rotulo.config(text = "você clicou botão 1")


def clique2():
    rotulo.config(text = "você clicou botão 2")

botão = tk.Button(janela, text= "botão 1", width=15, bg="red", font=("Arial", 10), command= clique)
botão.pack(padx=10, pady=10)

btn2 = tk.Button(janela, text= "botão 2", width=15, bg="pink", font=("Arial", 13), command= clique2)
btn2.pack(padx=10, pady=10)

janela.mainloop()
