class contaBancaria:
    def _init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.__saldo = saldo
    
    def depositar (self, valor_deposito):
        self.__saldo += valor_deposito
        return self.__saldo
    
    def sacar (self, valor_saque):
        if valor_saque <= self.__saldo:
            self.__saldo -= valor_saque
            print("Saque de R$ ", valor_saque)
        else:
            print("Saldo insuficiente.")

    def acao(self):
            self.numero_conta = int(input("Digite número da conta: "))
            self.__saldo = float(input("Digite o saldo da sua conta: "))
            acao = input("Você deseja fazer um deposito ou um saque? ")
            if acao == "deposito":
                valor_deposito = int(input("Quanto você deseja depositar? "))
                self.__saldo = self.depositar(valor_deposito)
            elif acao == "saque":
                valor_saque = float(input("Quanto você deseja sacar? "))
                self.__saldo = self.__saldo(valor_saque)

    def get_saldo(self): 
        return self.__saldo

        
minhaconta = contaBancaria()
minhaconta.acao()
minhaconta.get_saldo()