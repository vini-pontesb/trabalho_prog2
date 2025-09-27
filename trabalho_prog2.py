from datetime import datetime, date
import random as rd

class Cliente:
    def __init__(self, nome, email, idade, cpf):
        self._nome = nome
        self._email = email
        self._idade = idade
        self._cpf = cpf
        self.saldo = 0
        self._bancos = ["Itaú", "Banco do Brasil",
                        "Bradesco", "Caixa", "Santander"]
        self.extrato = []
        self.cheque_especial = 500
        self.taxa_confeccao = 600
        self.taxa_juros_mensal = 0.02
        self.taxa_seguro = 50

    def banks(self):
        self.banco_escolhido = rd.choice(self._bancos)

    def append(self):
        self.extrato.append({
            "Data": self.dataDep,
            "Banco": self.banco_escolhido,
            "Transação": self.transacao,
            "Nome": self._nome,
            "CPF": self._cpf,
            "Valor do Depósito": self.valorDep,
            "Saldo": self.saldo
        })

    def sacar(self, valorSaq, dataSaq=date.today()):
        self.valorSaq = valorSaq
        if dataSaq == date.today():
            data_formatada = dataSaq.strftime("%d/%m/%Y")
            self.dataSaq = datetime.strptime(data_formatada, "%d/%m/%Y").date()
        else:
            self.dataSaq = datetime.strptime(dataSaq, "%d/%m/%Y").date()
        self.transacao = "Saque"
        if valorSaq <= self.saldo and self.saldo:
            self.saldo -= valorSaq
            print(
                f"Você fez um saque de R${self.valorSaq} e está com R${self.saldo} na conta")
        elif valorSaq > self.saldo:
            valorSaq -= self.saldo
            self.saldo = 0
            self.cheque_especial -= valorSaq
            print(
                f"Você utilizou o cheque especial, agora seu saldo é de R${self.saldo} e seu chque especial é R${self.cheque_especial}")
        elif valorSaq > self.saldo + self.cheque_especial:
            print("Você não  possui mais saldo nem conta nem cheque especial")
        cliente1.append()

    def depositar(self, valorDep, dataDep=date.today()):
        self.valorDep = valorDep
        self.saldo = valorDep + self.saldo
        if dataDep == date.today():
            data_formatada = dataDep.strftime("%d/%m/%Y")
            self.dataDep = datetime.strptime(data_formatada, "%d/%m/%Y").date()
        else:
            self.dataDep = datetime.strptime(dataDep, "%d/%m/%Y").date()
        self.transacao = "Despósito"
        cliente1.append()
        print(
            f"Você fez um depósito de R${self.valorDep} e está com R${self.saldo} na conta")

    def mostrar_extrato(self, dataInicial, dataFinal):
        extrato_filtrado = []
        for transacao in self.extrato:
            if dataInicial <= transacao["Data"] <= dataFinal:
                extrato_filtrado.append(transacao)
        print(extrato_filtrado)

    def conta(self):
        print(
            f"Seu saldo atual no banco {self.banco_escolhido} é {self.saldo}")
    
    def simular_financiamento(self, valor, nParcelas):
        self.valorParcial = valor + self.taxa_confeccao
        self.price = (self.valorParcial * self.taxa_juros_mensal)/(1-(1/((1+self.taxa_juros_mensal)**nParcelas)))
        self.valorParcela = self.price + self.taxa_seguro
        self.valorTotal = self.valorParcela * nParcelas
        print(
            f"O valor da parcela será de R${self.valorParcela:.2f}, pagos em {nParcelas} meses, formando um total de R${self.valorTotal:.2f} a ser pago")

name = input("Insira o seu nome: ")
eMAIL = input("Insira seu email: ")
age = int(input("Insira sua idade: "))
CPF = int(input("Insira seu CPF: "))
cliente1 = Cliente(name, eMAIL, age, CPF)
cliente1.banks()
pergunta = int(input(
    "Siga as instruções:\n1 - Saque\n2 - Depósito\n3 - Exibir extrato\n4 - Exibir saldo atual\n5 - Simular financiamento\n-> "))
while pergunta != 1 and pergunta != 2 and pergunta != 3 and pergunta != 4 and pergunta != 5:
    print("Você não seguiu as regras, tente novamente!")
    pergunta = int(input(
        "Siga as instruções:\n1 - Saque\n2 - Depósito\n3 - Exibir extrato\n4 - Exibir saldo atual\n5 - Simular financiamento\n-> "))

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
            cliente1.sacar(saque, data)
        if duvida == 2:
            cliente1.sacar(saque)
    elif pergunta == 2:
        deposito = float(input("Insira em reais o valor do depósito: R$"))
        duvida = int(input("1 - Inserir data\n2 - Usar data de hoje\n-> "))
        while duvida != 1 and duvida != 2:
            print("Você não seguiu as regras, tente novamente!")
            duvida = int(input("1 - Inserir data\n2 - Usar data de hoje\n-> "))
        if duvida == 1:
            data = input("Insira a data do depósito (DD/MM/AAAA): ")
            cliente1.depositar(deposito, data)
        if duvida == 2:
            cliente1.depositar(deposito)
    elif pergunta == 3:
        DateStr1 = input("Insira a data inicial (DD/MM/AAAA): ")
        Date1 = datetime.strptime(DateStr1, "%d/%m/%Y").date()
        DateStr2 = input("Insira a data final (DD/MM/AAAA): ")
        Date2 = datetime.strptime(DateStr2, "%d/%m/%Y").date()
        cliente1.mostrar_extrato(Date1, Date2)
    elif pergunta == 4:
        cliente1.conta()
    elif pergunta == 5:
        valor_desejado = float(input("Insira o valor desejado: R$"))
        parcela = int(input("Insira o valor das parcelas: "))
        cliente1.simular_financiamento(valor_desejado, parcela)

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
