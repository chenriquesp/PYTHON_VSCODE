menu = """
#### Sistema Bancário ####

Selecione sua opção:

   [d] Depositar
   [s] Sacar
   [e] Extrato
   [q] Sair

-> """

saldo = 0.0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
quantidade_saques = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor a ser depositado : "))
        if valor > 0:
            saldo += valor
            print(f"Obrigado, você depositou R${valor: .2f}\n")
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.\n")

    elif opcao == "s":
        valor = float(input("informe valor a ser sacado: "))

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
           

    elif opcao == "e":
        print("################ EXTRATO ################\n")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Seu Saldo atual é R$ {saldo:.2f}\n")
        print("#########################################\n")

    elif opcao == "q":
        print("Obrigado por usar o nosso Sitema Bancário.")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.\n")
