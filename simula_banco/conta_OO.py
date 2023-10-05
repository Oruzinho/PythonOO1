class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Criando conta...\n {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print("Conta criada", end="\n\n")

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

    def extrato(self):
        print(
            "Titular: {} \n  Saldo: {}".format(self.__titular, self.__saldo), end="\n\n"
        )

    def depositar(self, valor):
        print("O Titular {} depositou {} reais".format(self.__titular, valor))
        print("O saldo antes do depósito era de {}".format(self.__saldo))
        self.__saldo += valor
        print("O novo saldo é de {}".format(self.__saldo), end="\n\n")

    def __verificar_saque(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def sacar(self, valor):
        if(self.__verificar_saque(valor)):
            print("O Titular {} sacou {} reais".format(self.__titular, valor))
            print("O saldo antes do saque era de {}".format(self.__saldo))
            self.__saldo -= valor
            print("O novo saldo é de {}".format(self.__saldo), end="\n\n")
        else:
            print("O valor ultrapassa o disponível na sua conta")

    def transferir(self, valor, destino):
        print(
            "Iniciando tranferência da conta do titular {} para a conta do titular {} no valor de {}".format(
                self.__titular, destino.__titular, valor
            )
        )
        self.sacar(valor)
        destino.depositar(valor)
        print("Transferência concluída com sucesso")

Conta.codigo_banco()

conta_1 = Conta(123, "Victor", 100.0)
conta_2 = Conta(321, "João", 50.0)

conta_1.extrato()
conta_2.extrato()


conta_1.depositar(100.0)
conta_2.sacar(20.0)

conta_1.transferir(10.0, conta_2)
