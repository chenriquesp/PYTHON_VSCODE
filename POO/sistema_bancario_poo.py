from abc import ABC, abstractmethod, abstractproperty

class Transacao(ABC):

    def registrar(self, conta):
        pass


class Deposito(Transacao):
    _valor = 0.00

    pass


class Saque(Transacao):
    _valor = 0.00

    pass


class Historico:
    def adicionar_transacao(self, transacao):
        pass


class Cliente:
    _endereco = ""
    _contas = []

    def realizar_transacao(self, conta, transacao):
        pass

    def adcionar_conta(self, conta):
        pass


class Conta:
    _saldo = 0.00
    _numero = 0
    _agencia = ""
    _cliente = Cliente()
    _historico = Historico()

    def saldo(self):
        return self._saldo

    @property
    def nova_conta(self, cliente, numero):
        conta = Conta()
        return conta

    def sacar(self, valor):
        return True

    def depositar(self, valor):
        return True


class PessoaFisica(Cliente):
    _cpf = ""
    _nome = ""
    _data_nascimento = 0

