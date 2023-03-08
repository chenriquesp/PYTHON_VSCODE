LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0.0
limite = 500
extrato = ""
quantidade_saques = 0
usuarios = []
contas = []

def menu():
    return input("""
    #### Sistema Bancário ####

    Selecione sua opção:

    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\t\tSair

    => """)

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
    usuario["data_nascimento"] = input("Insira a data de nascimento do Usuário(dd/mm/aaaa): ")
    usuario["endereco"] = input("Insira o endereço do Usuário (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append(usuario)
    print("Usuário inserido com sucesso.")

def cadastrar_conta(contas, agencia=AGENCIA):
    conta = {}

    cpf = input("Informe o CPF do Titular da C/C: ")
    usuario = listar_usuario(cpf)
    if not usuario:
        print("Usuário não existe, favor cadastrar Usuário primeiro.")
        return

    conta["numero"] = len(contas) + 1
    conta["agencia"] = agencia
    conta["usuario"] = usuario

    contas.append(conta)
    numero_conta = conta["numero"]

    print(f"\nConta {numero_conta} inserida com sucesso.")

def listar_usuario(cpf, usuarios=usuarios):
    for item in usuarios:
        if item["cpf"] == cpf:
            return item 
    return

def listar_conta(contas=contas):
    if not len(contas):
        print("Não existe contas cadastradas.")
        return

    print("#############################################\n")

    for conta in contas:
        print("#########################################################\n")
        print("Agencia:\t" + conta["agencia"])
        print("C/C:\t\t" + str(conta["numero"]))
        print("Titular:\t" + conta["usuario"]["nome"] + "\n")

def main():
    while True:

        opcao = menu()

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
            cadastrar_conta(contas)
        
        elif opcao == "lc":
            listar_conta()
        
        elif opcao == "nu":
            cadastrar_usuario()
        
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.\n")
        
main()