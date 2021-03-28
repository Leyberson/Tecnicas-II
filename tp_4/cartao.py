class Cartao:
    def __init__(self):
        self.limite_total = 1000
        self.limite_utilizado = 0
        self.valor_fatura = 0

    def comprar(self, valor, total_de_parcelas):
        self.limite_utilizado+=valor
        acrescimo = valor/total_de_parcelas
        self.valor_fatura += acrescimo

    def get_valor_fatura(self):
        if self.limite_utilizado == 0:
            return 0
        else:
            return self.valor_fatura
