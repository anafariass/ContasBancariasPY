class Conta:
    def __init__(self, numero, titular, saldo_inicial=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial

#verifica se o valor p depositar é valido.
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor

#verifica se é valido, se há saldo suficiente e se tiver retira.
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor

# verifica quanto tem
    def consultar_saldo(self):
        return self.saldo

#
class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo_inicial=0, limite=0):
        super().__init__(numero, titular, saldo_inicial)
        self.limite = limite

# Ele permite que o saque dinheiro e também considera o limite da conta.       
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo + self.limite:
            raise ValueError("Saldo e limite insuficientes.")
        self.saldo -= valor

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo_inicial=0, taxa_juros=0.01):
        super().__init__(numero, titular, saldo_inicial)
        self.taxa_juros = taxa_juros

#calcula os juros com base no saldo atual e adiciona no saldo.
    def render_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros


class ContaEmpresarial(Conta):
    def __init__(self, numero, titular, saldo_inicial=0, limite=0, taxa_juros=0.02):
        super().__init__(numero, titular, saldo_inicial)
        self.limite = limite
        self.taxa_juros = taxa_juros

#mesma forma que funciona nas outras
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo + self.limite:
            raise ValueError("Saldo e limite insuficientes.")
        self.saldo -= valor

    def render_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros 
