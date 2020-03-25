from src.buyer.buyer import Buyer
from wallet import PesosWallet, BitcoinWallet


def main():
    ars_wallet = PesosWallet(1000)
    btc_wallet = BitcoinWallet(0)
    buy_handler = Buyer(ars_wallet, btc_wallet)
    print(buy_handler.withdraw_from)
    print(buy_handler.deposit_to)


if __name__ == "__main__":
    print("[BUYER] Loading...")
    main()
    print("[BUYER] Done!")
