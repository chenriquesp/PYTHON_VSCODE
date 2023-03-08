from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self._valor): # o retorno do metodo depositar() é um boleando True para realizado e False se deu erro.
            conta.historico.adcionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.sacar(self._valor): # o retorno do metodo sacar() é um boleando True para realizado e False se deu erro.
            conta.historico.adcionar_transacao(self)


class Historico:
    def __init__(self) -> None:
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        #Copiei do professor pois não consegui resolver esta parte.
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adcionar_conta(self, conta):
        self._contas.append(conta)
    
    @property
    def contas(self):
        return self._contas
    
    @property
    def endereco(self):
        return self._endereco

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def data_nascimento(self):
        return self._data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def client(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.\n")
            return False
        elif valor > 0:
            saldo -= valor # Decrementa o valor do saldo da conta
            print(f"Você sacou R${valor: .2f}\n")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.\n")
        return False

    def depositar(self, valor):
        if valor > 0:
            saldo += valor # Incrementa o valor no saldo da conta
            print(f"Obrigado, você depositou R${valor: .2f}\n")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.\n")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saque

    def sacar(self, valor): # Demorou um pouco mas consegui adaptar meu método aqui
        quantidade_saques = 0

        for transacao in self.historico.tansacoes: #Com o apoio do professo eu consegui montar a busca
            if transacao["tipo"] == "Saque":
                quantidade_saques += 1

        if quantidade_saques > self._limite_saque:
            print("Operação falhou! Número máximo de saque excedido.\n")
            return False
        elif valor > self._limite:
            print("Operação falhou! O valor excede o limite.\n")
            return False
        
        super().sacar(valor)
    
    def __str__(self) -> str:
        return f"""
            Agência:\t{self.agencia}
            C\c:\t\t{self.numero}
            Titular:\t{self.client.nome}
        """

