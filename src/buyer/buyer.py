from src.wallet.wallet import Wallet


class Buyer:
    """
    This class handles the buy of any currency, you need to set the following:
    * wallet from where currencies will be withdrawn,
    * target wallet to deposit the currencies bought
    * transaction fee
    """

    def __init__(self, withdraw_wallet: Wallet, deposit_wallet: Wallet, transaction_fee: float):
        self.__withdraw_wallet = withdraw_wallet
        self.__deposit_wallet = deposit_wallet
        self.__transaction_fee = transaction_fee

    @property
    def withdraw_from(self) -> Wallet:
        return self.__withdraw_wallet

    @withdraw_from.setter
    def withdraw_from(self, wallet: Wallet):
        self.__withdraw_wallet = wallet

    @property
    def deposit_to(self) -> Wallet:
        return self.__deposit_wallet

    @deposit_to.setter
    def deposit_to(self, wallet: Wallet):
        self.__deposit_wallet = wallet

    @property
    def transaction_fee(self):
        return self.__transaction_fee

    def buy(self, amount):
        # TODO: Need to know how much currency costs to buy another currency
        # TODO: Validate withdraw_wallet has enough currency for transaction
        print("[BUYER] Buy transaction in progress...")
        self.withdraw_from.withdraw(amount + self.transaction_fee * amount)
        self.deposit_to.deposit(amount)
        print(f"[BUYER] Successfully bought {self.deposit_to.currency}: {amount}")
