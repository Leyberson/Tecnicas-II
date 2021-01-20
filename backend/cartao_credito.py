class Cartao_credito():
    def __init__(self, limite_total=1000):
        self.limite_total = limite_total
        self.limite_disponivel = limite_total
        self.valor_fatura = 0
        self.faturas_pagas = []
        self.faturas_a_vencer=[]
    
    def compra(self, valor, total_parcelas):
        if valor<=self.limite_disponivel:
            self.limite_disponivel-=valor
            valor_acrescentado= valor/total_parcelas
            self.valor_fatura = valor_acrescentado
            for i in range(0, total_parcelas):
                if len(self.faturas_a_vencer)>i:
                    self.faturas_a_vencer[i] += valor_acrescentado
                else:
                    self.faturas_a_vencer.append(valor_acrescentado)
        else:
            raise('transacao negada')

    def get_valor_fatura(self):
        return self.valor_fatura

    def aumetar_limite(self, valor):
        self.limite_total += valor
        self.limite_disponivel += valor
        