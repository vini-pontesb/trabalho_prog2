from cliente import Cliente


name = input("Insira o seu nome: ")
eMAIL = input("Insira seu email: ")
age = int(input("Insira sua idade: "))
CPF = int(input("Insira seu CPF: "))
cliente1 = Cliente(name, eMAIL, age, CPF)

pergunta = int(input(
    "Siga as instruções:\n1 - Saque\n2 - Depósito\n3 - Exibir extrato\n4 - Simular financiamento\n-> "))
while pergunta != 1 and pergunta != 2 and pergunta != 3 and pergunta != 4:
    print("Você não seguiu as regras, tente novamente!")
    pergunta = int(input(
        "Siga as instruções:\n1 - Saque\n2 - Depósito\n3 - Exibir extrato\n4 - Simular financiamento\n-> "))

interacao = True
while interacao == True:

    if pergunta == 1:
        saque = float(input("Insira em reais o valor do saque: R$"))
        duvida = int(input("1 - Inserir data\n2 - Usar data de hoje\n-> "))

        while duvida != 1 and duvida != 2:
            print("Você não seguiu as regras, tente novamente!")
            duvida = int(input("1 - Inserir data\n2 - Usar data de hoje\n-> "))

        if duvida == 1:
            data = input("Insira a data do saque (DD/MM/AAAA): ")
            status, saldo, cheque = cliente1.sacar(saque, data)
        elif duvida == 2:
            status, saldo, cheque = cliente1.sacar(saque)

        if status == "SAQUE":
            print(
                f"Você fez um saque de R${saque} e está com R${saldo} na conta")
        elif status == "CHEQUE ESPECIAL":
            print(
                f"Você utilizou o cheque especial para fazer um saque de R${saque}, agora seu saldo é de R${saldo} e seu cheque especial é R${cheque}")
        elif status == "FALHA":
            print(
                f"Você tentou fazer um saque de R${saque}, porém seu saldo e cheque especial somam R${saldo+cheque}")

    elif pergunta == 2:
        deposito = float(input("Insira em reais o valor do depósito: R$"))
        duvida = int(input("1 - Inserir data\n2 - Usar data de hoje\n-> "))

        while duvida != 1 and duvida != 2:
            print("Você não seguiu as regras, tente novamente!")
            duvida = int(input("1 - Inserir data\n2 - Usar data de hoje\n-> "))

        if duvida == 1:
            data = input("Insira a data do depósito (DD/MM/AAAA): ")
            saldo = cliente1.depositar(deposito, data)

        if duvida == 2:
            saldo = cliente1.depositar(deposito)

        print(
            f"Você fez um depósito de R${deposito} e seu saldo atual é R${saldo}")

    elif pergunta == 3:
        dateStr1 = input("Insira a data inicial (DD/MM/AAAA): ")
        dateStr2 = input("Insira a data final (DD/MM/AAAA): ")
        extrato = cliente1.mostrar_extrato(dateStr1, dateStr2)
        print(extrato)

    elif pergunta == 4:
        valor_desejado = float(input("Insira o valor desejado: R$"))
        parcela = int(input("Insira o valor das parcelas: "))
        vp, np, vt = cliente1.simular_financiamento(valor_desejado, parcela)
        print(
            f"O valor da parcela será de R${vp:.2f}, pagos em {np} meses, formando um total de R${vt:.2f} a ser pago")

    interacao = int(input(
        "Siga as intruções:\n1 - Para continuar na sessão\n2 - Para interromper a sessão\n-> "))

    while interacao != 1 and interacao != 2:
        print("Você não seguiu as regras, tente novamente!")
        interacao = int(input(
            "Siga as intruções:\n1 - Para continuar na sessão\n2 - Para interromper a sessão\n-> "))

    if interacao == 1:
        interacao = True
        pergunta = int(input(
            "Siga as instruções:\n1 - Saque\n2 - Depósito\n3 - Exibir extrato\n4 - Simular financiamento\n-> "))

    elif interacao == 2:
        interacao == False

print("Sua sessão terminou!")