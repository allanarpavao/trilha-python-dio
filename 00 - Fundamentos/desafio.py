
menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair

==>
"""

saldo = 0
limite = 500
extrato = ""
num_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Qual valor gostaria de depositar?"))
        if deposito < 0:
            print("Operação cancelada. O valor informado é inválido")
        else:
            saldo += deposito
            extrato += f"Depósito de R$ {deposito:.2f}\n"
            print("Seu saldo é R$ {:.2f}".format(saldo))

    elif opcao == "s":
        saque = float(input("Qual valor gostaria de sacar?"))
        
        
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_num_saques = num_saques >= limite_saques

        if excedeu_num_saques:
            print("Você atingiu o limite de saques diários.")

        elif excedeu_limite:
            print("Você atingiu o limite da operação de saque. Limite diário de R$500,00")

        elif excedeu_saldo:
            print("Saldo insuficiente. Seu saldo é R$ {:.2f}".format(saldo))
        
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque de R$ {saque:.2f}\n"
            num_saques += 1
            print("Você sacou R$ {:.2f}. Seu saldo atual é {:.2f}".format(saque, saldo))
            
        else:
            print("Operação cancelada. O valor informado é inválido")
                    
    elif opcao == "e":
        print("\n============= EXTRATO =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("Saldo: {:.2f}".format(saldo))
        print("===================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor selecione novamente a operação desejada.")
