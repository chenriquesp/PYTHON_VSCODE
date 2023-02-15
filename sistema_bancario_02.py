menu = """
#### Sistema Bancário ####

Selecione sua opção:

   [d]\tDepositar
   [s]\tSacar
   [e]\tExtrato
   [nc]\tNova Conta
   [lc]\tListar Contas
   [nu]\tNovo Usuário
   [q]\tSair

=> """

saldo = 0.0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
quantidade_saques = 0
usuarios = []
contas = []
AGENCIA = "0001"

def depositar( saldo, extrato, valor, /):
    if valor > 0:
        saldo += valor
        print(f"Obrigado, você depositou R${valor: .2f}\n")
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.\n")
    
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, limite_saque, quantidade_saques):
    LIMITE_SAQUES = limite_saque

    if quantidade_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saque excedido.\n")
    
    elif valor > limite:
        print("Operação falhou! O valor excede o limite.\n")

    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.\n")

    elif valor > 0:
        saldo -= valor
        print(f"Você sacou R${valor: .2f}\n")
        extrato += f"Saque: R$ {valor:.2f}\n"
        quantidade_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.\n")
    return saldo, extrato

def emitir_extrato(extrato,/ , *, saldo):
    print("################ EXTRATO ################\n")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Seu Saldo atual é R$ {saldo:.2f}\n")
    print("#########################################\n")
    return

def cadastrar_usuario(usuarios=usuarios):
    usuario = {}

    cpf = input("Informe o CPF do usuário(somente números): ")
    if listar_usuario(cpf):
        print("Usário já existe!")
        return
    usuario["cpf"] = cpf
    usuario["nome"] = input("Insira o nome do Usuário: ")
    usuario["data_nascimento"] = input("Insira a data de nascimento do Usuário: ")
    usuario["endereco"] = input("Insira o endereço do Usuário (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append(usuario)
    print("Usuário inserido com sucesso.")

def cadastrar_conta(contas=contas, agencia=AGENCIA):
    conta = {}

    cpf = input("Informe o CPF do usuário: ")
    usuario = listar_usuario(cpf)
    if not usuario:
        print("Usuário não existe, favor cadastrar Usuário primeiro.")
        return

    conta["numero"] = len(contas) + 1
    conta["agencia"] = agencia
    conta["usuario"] = usuario

    print("Conta inserido com sucesso.")

def listar_usuario(cpf, usuarios=usuarios):
    for item in usuarios:
        if item["cpf"] == cpf:
            return item
    
    return

def listar_conta(contas=contas):
    # if not len(contas):
    #     print("Não existe contas cadastradas.")
    #     return

    print("#############################################\n")

    for conta in contas:
        print(" conta: " + conta["numero"])
        print("Agencia: " + conta["agencia"])
        print("Usuário: " + conta["usuario"]["nome"])


while True:

    opcao = input(menu)

    if opcao == "d":
        
        valor = float(input("informe o valor a ser depositado : "))

        saldo, extrato = depositar(saldo, extrato, valor)

    elif opcao == "s":
        valor = float(input("informe valor a ser sacado: "))

        saldo, extrato = sacar(
            saldo= saldo, 
            valor= valor, 
            extrato= extrato, 
            limite= limite, 
            limite_saque= LIMITE_SAQUES, 
            quantidade_saques= quantidade_saques)
                  
    elif opcao == "e":
       emitir_extrato(extrato, saldo=saldo)

    elif opcao == "q":
        print("Obrigado por usar o nosso Sitema Bancário.")
        break

    elif opcao == "nc":
        cadastrar_conta()
    
    elif opcao == "lc":
        listar_conta()
    
    elif opcao == "nu":
        cadastrar_usuario()
    
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.\n")