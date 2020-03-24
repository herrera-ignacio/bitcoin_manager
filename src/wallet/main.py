from wallet import PesosWallet


def main():
    ars_wallet = PesosWallet(100)
    print(ars_wallet.amount)
    print("Wallet ON")


if __name__ == "__main__":
    main()
