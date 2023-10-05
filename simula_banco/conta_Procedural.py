def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def depositar(conta, valor):
    conta["saldo"] += valor


def sacar(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("O saldo da conta é {}".format(conta["saldo"]))


conta = cria_conta(123, "Victor", 55, 1000.0)
depositar(conta, 50.0)
sacar(conta, 100.0)
extrato(conta)
