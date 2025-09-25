import datetime as dt
import random as rd
# Número da Agência e Conta; Nome do Titular; Data e Hora da Consulta; CPF

while True:
    try:
        class Cliente:
            def __init__(self, nome, email, idade, cpf):
                self.nome = nome
                self.email = email
                self.idade = idade
                self.cpf = cpf
                self.saldo = 0
                self.bancos = ["Itaú", "Banco do Brasil",
                               "Bradesco", "Caixa", "Santander"]
                self.extrato = []

            def banks(self):
                self.banco_escolhido = rd.choice(self.bancos)

            def depositar(self, valorDep, dataDep):
                self.valorDep = valorDep
                self.saldo = valorDep + self.saldo
                self.dataDep = dataDep
                self.transacao = "Despósito"
                self.extrato.append({
                    "Data": self.dataDep,
                    "Banco": self.banco_escolhido,
                    "Transação": "Depósito",
                    "Nome": self.nome,
                    "CPF": self.cpf,
                    "Valor do Depósito": self.valorDep
                })
                print(
                    f"Você fez um depósito de R${self.valorDep} e está com R${self.saldo} na conta")

            def sacar(self, valorSaq, dataSaq):
                self.valorSaq = valorSaq
                self.saldo = self.saldo - valorSaq
                self.dataSaq = dataSaq
                self.transacao = "Saque"
                self.extrato.append({
                    "Data": self.dataSaq,
                    "Transação": "Saque",
                    "Banco": self.banco_escolhido,
                    "Nome": self.nome,
                    "CPF": self.cpf,
                    "Valor do Saque": self.valorSaq,
                })
                print(
                    f"Você fez um saque de R${self.valorSaq} e está com R${self.saldo} na conta")

            def mostrar_extrato(self, dataInicial, dataFinal):
                extrato_filtrado = []
                for transacao in self.extrato:
                    if dataInicial <= transacao["Data"] <= dataFinal:
                        extrato_filtrado.append(transacao)
                print(extrato_filtrado)

            def conta(self):
                print(
                    f"Seu saldo atual no banco {self.banco_escolhido} é {self.saldo}")

        name = input("Insira o seu nome: ")
        eMAIL = input("Insira seu email: ")
        age = int(input("Insira sua idade: "))
        CPF = int(input("Insira seu CPF: "))
        pergunta = int(input(
            "Siga as instruções:\n1 - Saque\n2 - Depósito\n3 - Exibir extrato\n4 - Exibir saldo atual\n-> "))
        cliente1 = Cliente(name, eMAIL, age, CPF)
        cliente1.banks()

        interacao = True
        while interacao == True:
            if pergunta == 1:
                saque = float(input("Insira em reais o valor do saque: "))
                data = dt.date.today()
                data_formatada = data.strftime("%d/%m/%Y")
                cliente1.sacar(saque, dt.datetime.strptime(
                    data_formatada, "%d/%m/%Y").date())
            elif pergunta == 2:
                deposito = float(
                    input("Insira em reais o valor do depósito: "))
                data = dt.date.today()
                data_formatada = data.strftime("%d/%m/%Y")
                cliente1.depositar(deposito, dt.datetime.strptime(
                    data_formatada, "%d/%m/%Y").date())
            elif pergunta == 3:
                DateStr1 = input("Insira a data inicial (DD/MM/AAAA): ")
                Date1 = dt.datetime.strptime(DateStr1, "%d/%m/%Y").date()
                DateStr2 = input("Insira a data final (DD/MM/AAAA): ")
                Date2 = dt.datetime.strptime(DateStr2, "%d/%m/%Y").date()
                cliente1.mostrar_extrato(Date1, Date2)
            elif pergunta == 4:
                cliente1.conta()
            else:
                print("Você não fez o que foi pedido!")
            interacao = int(input(
                "Siga as intruções:\n1 - Para continuar na sessão\n2 - Para interromper a sessão\n-> "))
            while interacao != 1 and interacao != 2:
                print("Você não seguiu as regras, tente novamente!")
                interacao = int(input(
                    "Siga as intruções:\n1 - Para continuar na sessão\n2 - Para interromper a sessão\n-> "))
            if interacao == 1:
                interacao = True
                pergunta = int(input(
                    "Siga as instruções:\n1 - Saque\n2 - Depósito\n3 - Exibir extrato\n4 - Exibir saldo atual\n-> "))
            elif interacao == 2:
                interacao == False
        print("Sua sessão terminou!")
        break
    except ValueError:
        print("Você inseriu um valor errado, tente novamnete!")
