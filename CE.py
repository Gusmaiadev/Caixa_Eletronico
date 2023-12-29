def inicializar_conta():
    return 0


def realizar_deposito(saldo, valor):
    saldo += valor
    return saldo


def realizar_saque(saldo, valor):
    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        print("Saque de R$ {:.2f} realizado com sucesso.".format(valor))
    return saldo


def exibir_saldo(saldo, saques, depositos):
    print("\n======= Extrato =======")
    print("Saldo atual: R$ {:.2f}".format(saldo))
    print("Total sacado: R$ {:.2f}".format(saques))
    print("Total depositado: R$ {:.2f}".format(depositos))
    print("=======================")


def main():
    saldo = inicializar_conta()
    saques = 0
    depositos = 0

    while True:
        print("\n===== Caixa Eletrônico =====")
        print("1. Realizar depósito")
        print("2. Realizar saque")
        print("3. Exibir saldo e extrato")
        print("4. Sair")

        opcao = int(input("Escolha uma opção (1-4): "))

        if opcao == 1:
            valor_deposito = float(input("Digite o valor do depósito: "))
            saldo = realizar_deposito(saldo, valor_deposito)
            depositos += valor_deposito
            print("Depósito realizado com sucesso.")

        elif opcao == 2:
            valor_saque = float(input("Digite o valor do saque: "))
            saldo = realizar_saque(saldo, valor_saque)
            saques += valor_saque

        elif opcao == 3:
            exibir_saldo(saldo, saques, depositos)

        elif opcao == 4:
            print("Saindo do caixa eletrônico. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
