from wallet import PesosWallet, DollarWallet, BitcoinWallet


def main():
    ars_wallet = PesosWallet(100)
    usd_wallet = DollarWallet(0)
    btc_wallet = BitcoinWallet(0)
    print("Wallet ON")


if __name__ == "__main__":
    main()
