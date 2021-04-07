import datetime as dt

class Cartao_credito:
    def __init__(self, limite_total=1000):
        self.limite_total = limite_total
        self.limite_disponivel = limite_total
        self.valor_fatura = 0
        self.faturas_pagas = []
        self.faturas_a_vencer = []
        self.faturas_a_vencidas = []
        self.compras = []

    def get_limite_disponivel(self):
        return self.limite_disponivel

    def set_limite_disponível(self, valor):
        self.limite_disponivel = valor

    def get_valor_fatura(self):
        return self.valor_fatura
    
    def compra(self, valor, total_parcelas):
        if valor <= self.limite_disponivel:
            self._realizar_compra(valor, total_parcelas)
        else:
            raise Exception('transacao negada')

    def _realizar_compra(self, valor, total_parcelas):
        data_transacao = dt.datetime.now()
        compra = Compra(valor, total_parcelas, data_transacao)
        self.compras.append(compra)
        self.limite_disponivel -= valor
        valor_acrescentado = valor / total_parcelas
        self._incrementar_faturas(valor_acrescentado, total_parcelas)

    def _incrementar_faturas(self, valor_incremento, total_parcelas):
        self.valor_fatura += valor_incremento
        for i in range(0, total_parcelas):
            if len(self.faturas_a_vencer) > i:
                self.faturas_a_vencer[i] += valor_incremento
            else:
                self.faturas_a_vencer.append(valor_incremento)


class Compra:
    def __init__(self, valor, total_parcelas, data_transacao, estabelecimento = None):
        self.valor = valor
        self.total_parcelas = total_parcelas
        self.data_transacao = data_transacao
        self.estabelecimento = estabelecimento

    def __eq__(self, other):
        return self.valor == other.valor and \
               self.total_parcelas == other.total_parcelas and \
               self.data_transacao == other.data_transacao and \
               self.estabelecimento == other.estabelecimento
