import pytest
from app.banco import Conta, ContaCorrente, ContaPoupanca, ContaEmpresarial

def test_conta_corrente():
    conta = ContaCorrente(1, 'João', 1000, 500)
    conta.depositar(200)
    assert conta.consultar_saldo() == 1200
    conta.sacar(1500)
    assert conta.consultar_saldo() == -300
    with pytest.raises(ValueError):
        conta.sacar(100)

def test_conta_poupanca():
    conta = ContaPoupanca(2, 'Maria', 1000, 0.05)
    conta.render_juros()
    assert conta.consultar_saldo() == 1050
    conta.depositar(200)
    assert conta.consultar_saldo() == 1250
    conta.sacar(250)
    assert conta.consultar_saldo() == 1000
    

def test_conta_empresarial():
    conta = ContaEmpresarial(3, 'Mercado 87', 2000, 1000, 0.03)
    conta.depositar(500)
    assert conta.consultar_saldo() == 2500
    conta.sacar(3000)
    assert conta.consultar_saldo() == -500
    conta.render_juros()
    assert conta.consultar_saldo() == -515
