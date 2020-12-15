class Conta():
    def __init__(self, numero):
        self.saldo_total = 0.0
        self.saldo_investido = 0.0
        self.saldo_disponivel= 0.0

        self.numero_conta=numero
        self.agencia=1

    def depositar(self, valor):
        self.saldo_total+=valor
        self.saldo_disponivel+=valor

    def sacar(self, valor):
        if self.saldo_disponivel>=valor:
            self.saldo_disponivel-=valor
        else:
            print('Desculpa, voce nao tem saldo o suficiente para realizar esse saque')
    
    def investir(self, valor):
        if self.saldo_disponivel>=valor:
            self.saldo_disponivel-=valor
            self.saldo_investido+=valor
        else:
            print('Desculpa, voce nao tem saldo o suficiente para realizar investir')

    def resgatar_investimento(self, valor):
        if self.saldo_investido>=valor:
            self.saldo_disponivel+=valor
            self.saldo_investido-=valor
        else:
            print('Desculpa, voce nao tem saldo o suficiente para realizar investir')
    
    def rende(self, porcentagem):
        juros = self.saldo_investido*porcentagem/100
        self.saldo_investido+=juros
        self.saldo_total+=juros