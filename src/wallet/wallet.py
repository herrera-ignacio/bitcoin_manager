class Wallet:
    __currency = None

    def __init__(self, amount: float = 0):
        self.__amount = amount

    @property
    def currency(self) -> str:
        return self.__currency

    @property
    def amount(self) -> float:
        return self.__amount

    def deposit(self, amount: float):
        self.__amount += amount

    def withdraw(self, amount: float):
        if self.amount - amount < 0:
            raise ValueError(f"Not enough {self.currency}.")
        else:
            self.amount -= amount


class PesosWallet(Wallet):
    __currency = "ARS"


class DollarWallet(Wallet):
    __currency = "USD"


class BitcoinWallet(Wallet):
    __currency = "BTC"

