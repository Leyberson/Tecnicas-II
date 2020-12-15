import sys
import os

# get parent directory
pwd = os.path.dirname(os.path.abspath((__file__)))
parent = os.path.dirname(pwd)
sys.path.append(parent)

#import conta
from backend.cartao_credito import Cartao_credito

class Mock_cartao():
    def get_valor_fatura(self):
        return 150

def test_criar_cartao():
    cartao = Cartao_credito()
    
    assert cartao.limite_disponivel == 1000
    assert cartao.limite_total == 1000
    assert cartao.valor_fatura == 0

def test_compa_sucesso():
    cartao = Cartao_credito()
    cartao.compra(500, 4)

    assert cartao.limite_disponivel == 500
    assert cartao.limite_total == 1000
    assert cartao.get_valor_fatura() == 125

def test_compa_falha():
    cartao = Cartao_credito()
    try:
        cartao.compra(1500, 4)
        raise('compra nao deveria ser efetuada')
    except:
        assert cartao.limite_disponivel == 1000
        assert cartao.limite_total == 1000
        assert cartao.get_valor_fatura() == 0

def test_valor_fatura():
    cartao = Cartao_credito()
    mock_cartao = Mock_cartao()

    cartao.compra(500, 10)
    cartao.compra(500, 5)
    valor_real = cartao.get_valor_fatura()
    valor_correto=mock_cartao.get_valor_fatura()

    assert valor_real == valor_correto
