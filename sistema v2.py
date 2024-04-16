import textwrap

def menu():
    menu = """
    =========== Menu ===========

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [u]\tNovo Usuário
    [c]\tNova Conta
    [l]\tListar Contas
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, extrato,/):

    valor = float(input("Insira quanto deseja depositar em R$: "))

    if valor > 0:
        saldo += valor
        print(f"Depósito realizado com sucesso.")
        extrato += f"Deposito de R$ {valor:.2f} \n"
    else:
        print("Valor inválido.")

    return(saldo, extrato)


def sacar(*,saldo, extrato, LIMITE_POR_SAQUE, numero_saques, LIMITE_DE_SAQUES):

    if numero_saques < LIMITE_DE_SAQUES:
        valor = float(input("Insira quanto deseja sacar em R$: "))

        if valor > saldo:
            print("Você não possui saldo suficiente.")

        elif valor > LIMITE_POR_SAQUE:
            print("Limite de R$ 500.00 por saque.")

        elif valor > 0:
            saldo -= valor
            print(f"Saque realizado com sucesso.")
            numero_saques += 1
            extrato += f"Saque de R$ {valor:.2f} \n"

        else:
            print("Valor inválido.")

    else:
        print('Limite de saques diários atingido.')

    return(saldo, extrato, numero_saques)


def exibir_extrato(saldo,/,*,extrato):

    print("============== Extrato ==============")
    print("Não foram realizadas operações" if not extrato else extrato)
    print(f"\nVocê possui atualmente R$ {saldo:.2f}")
    print("=====================================")


def cadastrar_usuario(usuarios):

    cpf = input("Insira o CPF: ")
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existe.")
        return

    nome = input("Insira o nome: ")
    data_nascimento = input("Insira a data de nascimento: ")
    endereco = input("Insira o endereço: ")

    usuarios.append({"cpf":cpf, "nome":nome, "data_nascimento":data_nascimento,"endereco":endereco})
    print("Usuário cadastrado com sucesso.")


def cadastrar_conta(AGENCIA, usuarios, numero):

    cpf = input("Insira o CPF do usuário: ")
    usuario = verificar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta cadastrada com sucesso. ")
        return {"agencia":AGENCIA, "numero":numero, "usuario":usuario}

    print("Usuário não existe.")


def verificar_usuario(cpf,usuarios):

    usuario_existe = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_existe[0] if usuario_existe else None


def main():

    saldo = 0
    extrato = ""
    numero_saques = 0
    LIMITE_DE_SAQUES = 3
    LIMITE_POR_SAQUE = 500
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == "d":

            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                LIMITE_POR_SAQUE=LIMITE_POR_SAQUE,
                numero_saques=numero_saques,
                LIMITE_DE_SAQUES=LIMITE_DE_SAQUES
            )

        elif opcao == "e":

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":

            cadastrar_usuario(usuarios)

        elif opcao == "c":
            
            numero = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, usuarios, numero)

            if conta:
                contas.append(conta)

        elif opcao == "l":

            for conta in contas:
                linha = f"""
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero']}
                Titular:\t{conta['usuario']['nome']}
                """
                print("=" * 28)
                print(textwrap.dedent(linha))

        elif opcao == "q":

            break

        else:
            print("Operação inválida, por favor insira novamente a operação desejada.")

main()
