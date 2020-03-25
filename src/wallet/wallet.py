class Wallet:
    """
    Currency Wallet [SINGLETON]
    """
    __wallet = None

    @classmethod
    def get_wallet(cls):
        if cls.__wallet is None:
            cls()
        return cls.__wallet

    def __init__(self, currency: str, funds: float = 0):
        if self.__class__.__wallet is not None:
            raise Exception("Wallet already created!")
        else:
            self.__funds = funds
            self.__currency = currency
            print(f"Creating wallet with {currency}: {funds}")
            self.__class__.__wallet = self

    @property
    def currency(self) -> str:
        return self.__currency

    @currency.setter
    def currency(self, name: str):
        self.__currency = name

    @property
    def funds(self) -> float:
        return self.__funds

    def deposit(self, amount: float):
        self.__funds += amount

    def withdraw(self, amount: float):
        if self.funds - amount < 0:
            raise ValueError(f"Not enough {self.currency}.")
        else:
            self.__funds -= amount


class PesosWallet(Wallet):
    def __init__(self, funds: float):
        super().__init__("ARS", funds)


class DollarWallet(Wallet):
    def __init__(self, funds: float):
        super().__init__("USD", funds)


class BitcoinWallet(Wallet):
    def __init__(self, funds: float):
        super().__init__("BTC", funds)

