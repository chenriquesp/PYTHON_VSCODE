class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor


conta = Conta(100)
conta.depositar(100)
print(conta._saldo)