from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import os

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
        if conta.depositar(self._valor): # o retorno do metodo depositar() é um boleando, True para realizado e False se deu erro.
            conta.historico.adicionar_transacao(self)
        else:
            print("Não registrou saque")


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if not conta.sacar(self._valor): # o retorno do metodo sacar() é um boleando, True para realizado e False se deu erro.
            # Está retornando False onde era pra ser True, por isso o 'not', não identidiquei motivo
            conta.historico.adicionar_transacao(self)
        else:
            print("Não registrou saque")


class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        # Copiei do professor pois não consegui resolver esta parte.
        # Houve a correção da string de entrada da data hora.
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
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
        if valor > self._saldo: # a valor a ser sacado não pode ser maior que o saldo
            print("Operação falhou! Você não tem saldo suficiente.\n")
            return False
        elif valor > 0:
            self._saldo -= valor # Decrementa o valor do saldo da conta
            print(f"Você sacou R${valor: .2f}\n")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.\n")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor # Incrementa o valor no saldo da conta
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

        for transacao in self.historico.transacoes: #Com o apoio do professo eu consegui montar a busca
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
            C\c:\t{self.numero}
            Titular:\t{self.client.nome}
        """


def depositar(clientes):

    cpf = input("Informe o CPF do cliente(somente números): ")
    cliente = listar_cliente(cpf, clientes)

    if not cliente:
        print("O Sitema não possui clientes cadastrados.")
        return
    
    valor = float(input("informe o valor a ser depositado: "))

    if valor < 0:
        print("Operação falhou! O valor informado é inválido.\n")
        return
    
    transacao = Deposito(valor)

    conta = retorna_conta_cliente(cliente)
    if not conta:
        print("Não existe conta para o Cliente.")
        return
    
    cliente.realizar_transacao(conta, transacao) 

def sacar(clientes):
    cpf = input("Informe o CPF do cliente(somente números): ")
    cliente = listar_cliente(cpf, clientes)

    if not cliente:
        print("O cliente não foi cadastrado.")
        return
    
    valor = float(input("informe o valor a ser Sacado: "))

    if valor < 0:
        print("Operação falhou! O valor informado é inválido.\n")
        return
    
    transacao = Saque(valor)

    conta = retorna_conta_cliente(cliente)
    if not conta:
        print("Não existe conta para o Cliente.")
        return
    
    cliente.realizar_transacao(conta, transacao)

def retorna_conta_cliente(cliente):
    contas = cliente.contas
    if not contas:
        return
    # O cliente não tem como escolher a conta, será revisto em uma nova atualização
    return contas[0]

def emitir_extrato(clientes):
    cpf = input("Informe o CPF do cliente(somente números): ")

    cliente = listar_cliente(cpf, clientes)
    if not cliente:
        print("O Cliente não foi cadastrado.")
        return
    
    conta = retorna_conta_cliente(cliente)
    if not conta:
        print("Não existe conta para o Cliente.")
        return
    
    print("################## EXTRATO ##################\n")
    transacoes = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato += "Não foram realizadas movimentações\n"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']} em {transacao['data']} R$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSeu Saldo atual é R$ {conta.saldo:.2f}")
    print("#############################################\n")

def cadastrar_cliente(clientes):

    cpf = input("Informe o CPF do cliente(somente números): ")
    if listar_cliente(cpf, clientes):
        print("Cliente já existe!")
        return
    nome            = input("Insira o nome do Cliente: ")
    data_nascimento = input("Insira a data de nascimento do Cliente(dd/mm/aaaa): ")
    endereco        = input("Insira o endereço do Cliente(logradouro, nro - bairro - cidade/sigla estado): ")
    
    cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)

    clientes.append(cliente)
    print("\nCliente inserido com sucesso.\n")

def cadastrar_conta(contas, clientes):

    cpf = input("Informe o CPF do Titular da C/C: ")
    cliente = listar_cliente(cpf, clientes)

    if not cliente:
        print("Usuário não existe, favor cadastrar um cliente primeiro.")
        return

    numero_conta = len(contas) + 1
    conta = ContaCorrente.nova_conta(numero_conta, cliente)

    contas.append(conta)
    cliente.adcionar_conta(conta)

    print(f"\nConta {numero_conta} inserida com sucesso.\n")

def listar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente 
    return

def listar_conta(contas):
    if not len(contas):
        print("Não existe contas cadastradas.\n")
        return

    for conta in contas:
        print("#########################################################")
        print(conta)
    print("#########################################################\n")

def menu():
    menu = """
    #### Sistema Bancário ####

    Selecione sua opção:

    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Cliente
    [q] \tSair

    => """
    pause_limpa_tela()

    return input(menu)

def main():
    clientes = []
    contas   = []

    while True:

        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)
            
            pass
                    
        elif opcao == "e":
            emitir_extrato(clientes)

        elif opcao == "q":
            print("Obrigado por usar o nosso Sitema Bancário.")
            break

        elif opcao == "nc":
            cadastrar_conta(contas, clientes)
        
        elif opcao == "lc":
            listar_conta(contas)
        
        elif opcao == "nu":
            cadastrar_cliente(clientes)
        
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.\n")

def pause_limpa_tela():
    # Criei esta função para limpara a tela e pausar esperando pressionar "Enter" para continuar
    # Funciona com o comando 'CLS' no Windows e o comando 'CLEAN' em LINUX e MAC
    
    input("Pressione 'Enter' para continuar...")
    os.system('cls') or None # Windows
    # os.system('clean') or None # Linux e MAC


main()
