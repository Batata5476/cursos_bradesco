class Conta:
    def __init__(self, titular, numero, saldo=0):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("O saldo não pode ser negativo")
        else:
            self._saldo = valor

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposita(self, valor):
        self._saldo += valor

    def extrato(self):
        print("Cliente:", self._titular, "| Saldo Atual:", self._saldo)
