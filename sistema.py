menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_DE_SAQUES = 3
LIMITE_POR_SAQUE = 500

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Insira quanto deseja depositar em R$: "))

        if deposito > 0:
            saldo += deposito
            print(f"Depósito realizado com sucesso.")
            extrato += f"Deposito de R$ {deposito:.2f} \n"

        else:
            print("Valor inválido.")

    elif opcao == "s":

        if numero_saques < LIMITE_DE_SAQUES:
            saque = float(input("Insira quanto deseja sacar em R$: "))

            if saque > saldo:
                print("Você não possui saldo suficiente.")

            elif saque > LIMITE_POR_SAQUE:
                print("Limite de R$ 500.00 por saque.")

            elif saque > 0:
                saldo -= saque
                print(f"Saque realizado com sucesso.")
                numero_saques += 1
                extrato += f"Saque de R$ {saque:.2f} \n"

            else:
               print("Valor inválido.")

        else:
            print('Limite de saques diários atingido.')

    elif opcao == "e":
        print("============== Extrato ==============")
        print("Não foram realizadas operações" if not extrato else extrato)
        print(f"\nVocê possui atualmente R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor insira novamente a operação desejada.")
