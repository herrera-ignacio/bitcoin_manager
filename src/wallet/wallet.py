class Wallet:
    """
    Currency Wallet [SINGLETON]
    """
    __currency = None
    __wallet = None

    @classmethod
    def get_wallet(cls):
        if cls.__wallet is None:
            cls()
        return cls.__wallet

    def __init__(self, amount: float = 0):
        if self.__class__.__wallet is not None:
            raise Exception("Wallet already created!")
        else:
            self.__amount = amount
            self.__class__.__wallet = self

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

