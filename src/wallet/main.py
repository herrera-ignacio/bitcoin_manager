from wallet import PesosWallet, DollarWallet, BitcoinWallet
from funds_manager import get_funds


def main():
    print("[WALLET] - OK")
    funds = get_funds()
    ars_wallet = PesosWallet(funds["ARS"])
    usd_wallet = DollarWallet(funds["USD"])
    btc_wallet = BitcoinWallet(funds["BTC"])


if __name__ == "__main__":
    main()
