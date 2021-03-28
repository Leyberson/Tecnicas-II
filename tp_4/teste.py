from cartao import Cartao

def teste_valor_fatura_sem_compra():
    cartao = Cartao()
    assert cartao.get_valor_fatura() == 0, ""


def teste_valor_fatura():
    cartao = Cartao()
    cartao.comprar(valor = 100, total_de_parcelas = 5)
    cartao.comprar(valor = 200, total_de_parcelas = 4)
    assert cartao.get_valor_fatura() == 70, "Valor incorreto"