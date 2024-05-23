class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
 
    def envelhecer(self,anos):
        self.idade += anos

    def crescer(self):
        if self.idade <21:
            self.altura+=0.5

pessoa= pessoa ("Maria, 20,70,170")
print(pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura)
pessoa.envelhecer(2)
pessoa.crescer()
print(f"nome:{pessoa.nome}, idade:{pessoa.idade}, peso:{pessoa.peso}, altura:{pessoa.altura}")