import sys
import os

# get parent directory
pwd = os.path.dirname(os.path.abspath((__file__)))
parent = os.path.dirname(pwd)
sys.path.append(parent)

#import conta
from backend.conta import Conta

def test_criacaoconta_saldo_disponivel():
    conta = Conta(2)

    assert 0.0 == conta.saldo_disponivel
    assert 0.0 == conta.saldo_investido
    assert 0.0 == conta.saldo_total
    
    assert 2 == conta.numero_conta
    assert 1 == conta.agencia

def test_depositar():
    conta = Conta(1)
    conta.depositar(100.0)

    assert 100.0 == conta.saldo_disponivel
    assert 100.0 == conta.saldo_total
    assert 0 == conta.saldo_investido

def test_saque_sucedido():
    conta = Conta(1)
    conta.depositar(100.0)
    conta.sacar(50.0)

    assert 50.0 == conta.saldo_disponivel
    assert 100.0 == conta.saldo_total
    assert 0 == conta.saldo_investido

def test_saque_falho():
    conta = Conta(1)
    conta.depositar(100.0)
    conta.sacar(200.0)
    
    assert 100.0 == conta.saldo_disponivel
    assert 100.0 == conta.saldo_total
    assert 0 == conta.saldo_investido

def test_investimento_sucesso():
    conta = Conta(1)
    conta.depositar(100)
    conta.investir(60)

    assert conta.saldo_disponivel == 40
    assert conta.saldo_investido == 60
    assert conta.saldo_total == 100

def test_investimento_falha():
    conta = Conta(1)
    conta.depositar(100)
    conta.investir(200)

    assert conta.saldo_disponivel == 100
    assert conta.saldo_investido == 0
    assert conta.saldo_total == 100

def test_resgatar_investimento_sucesso():
    conta = Conta(1)
    conta.depositar(100)
    conta.investir(50)
    conta.resgatar_investimento(40)

    assert conta.saldo_disponivel == 90
    assert conta.saldo_investido == 10
    assert conta.saldo_total == 100

def test_resgatar_investimento_falha():
    conta = Conta(1)
    conta.depositar(100)
    conta.investir(55)
    conta.resgatar_investimento(60)

    assert conta.saldo_disponivel == 45
    assert conta.saldo_investido == 55
    assert conta.saldo_total == 100

def test_rendimento():
    conta = Conta(1)
    conta.depositar(100)
    conta.investir(50)
    conta.rende(1)

    assert conta.saldo_total == 100.5
    assert conta.saldo_investido == 50.5
    assert conta.saldo_disponivel == 50