class Cartao_credito():
    def __init__(self, limite_total=1000):
        self.limite_total = limite_total
        self.limite_disponivel = limite_total
        self.valor_fatura = 0
    
    def compra(self, valor, total_parcelas):
        if valor<=self.limite_disponivel:
            self.limite_disponivel-=valor
            self.valor_fatura += valor/total_parcelas
        else:
            raise('transacao negada')

    def get_valor_fatura(self):
        return self.valor_fatura
        