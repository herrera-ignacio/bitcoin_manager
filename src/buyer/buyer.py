from src.wallet.wallet import Wallet


class Buyer:
    """
    This class handles the buy of any currency,
    you need to set the wallet from where currencies will be withdrawn
    and the target wallet to deposit the currencies bought
    """

    def __init__(self, withdraw_wallet: Wallet, deposit_wallet: Wallet):
        self.__withdraw_wallet = withdraw_wallet
        self.__deposit_wallet = deposit_wallet

    @property
    def withdraw_from(self) -> str:
        return self.__withdraw_wallet.currency

    @withdraw_from.setter
    def withdraw_from(self, wallet: Wallet):
        self.__withdraw_wallet = wallet

    @property
    def deposit_to(self) -> str:
        return self.__deposit_wallet.currency

    @deposit_to.setter
    def deposit_to(self, wallet: Wallet):
        self.__deposit_wallet = wallet

