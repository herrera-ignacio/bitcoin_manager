from src.buyer.buyer import Buyer
from wallet import PesosWallet, BitcoinWallet


def main():
    ars_wallet = PesosWallet(1000.0)
    btc_wallet = BitcoinWallet(0.0)
    buy_handler = Buyer(ars_wallet, btc_wallet, 0.01)
    buy_handler.buy(500.0)
    print(ars_wallet.funds)


if __name__ == "__main__":
    print("[BUYER] Loading...")
    main()
    print("[BUYER] Done!")
