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
        if self.transacao == "Depósito":
            self.extrato.append({
                "Data": self.dataDep,
                "Banco": self.banco_escolhido,
                "Transação": self.transacao,
                "Nome": self._nome,
                "CPF": self._cpf,
                "Valor do Depósito": self.valorDep,
                "Saldo": self.saldo
            })
        elif self.transacao == "Saque":
            self.extrato.append({
                "Data": self.dataSaq,
                "Banco": self.banco_escolhido,
                "Transação": self.transacao,
                "Nome": self._nome,
                "CPF": self._cpf,
                "Valor do Saque": self.valorSaq,
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
        if valorSaq <= self.saldo:
            self.saldo -= valorSaq
            self.append()
            return ("SAQUE", self.saldo, self.cheque_especial)
        elif valorSaq > self.saldo and valorSaq <= self.saldo + self.cheque_especial:
            valorSaq -= self.saldo
            self.saldo = 0
            self.cheque_especial -= valorSaq
            self.append()
            return ("CHEQUE ESPECIAL", self.saldo, self.cheque_especial)
        elif valorSaq > self.saldo + self.cheque_especial:
            return ("FALHA", self.saldo, self.cheque_especial)

    def depositar(self, valorDep, dataDep=date.today()):
        self.valorDep = valorDep
        self.saldo = valorDep + self.saldo
        if dataDep == date.today():
            data_formatada = dataDep.strftime("%d/%m/%Y")
            self.dataDep = datetime.strptime(data_formatada, "%d/%m/%Y").date()
        else:
            self.dataDep = datetime.strptime(dataDep, "%d/%m/%Y").date()
        self.transacao = "Despósito"
        self.append()
        return self.saldo

    def mostrar_extrato(self, data1, data2):
        dataInicial = datetime.strptime(data1, "%d/%m/%Y").date()
        dataFinal = datetime.strptime(data2, "%d/%m/%Y").date()
        extrato_filtrado = []
        for transacao in self.extrato:
            if dataInicial <= transacao["Data"] <= dataFinal:
                extrato_filtrado.append(transacao)
        return extrato_filtrado

    def simular_financiamento(self, valor, nParcelas):
        valorParcial = valor + self.taxa_confeccao
        price = (valorParcial * self.taxa_juros_mensal) / \
            (1-(1/((1+self.taxa_juros_mensal)**nParcelas)))
        valorParcela = price + self.taxa_seguro
        valorTotal = valorParcela * nParcelas
        return (valorParcela, nParcelas, valorTotal)