# from backend.conta import Conta

# from conta import Conta
import sys
import os

pwd = os.path.dirname(os.path.abspath((__file__)))
parent = os.path.dirname(pwd)
print(parent)
sys.path.append(parent)

from backend.conta import Conta

def test_criacaoconta():
    conta = Conta()

    assert 0.0 == conta.saldo