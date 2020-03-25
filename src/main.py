from wallet import main as wallet
from buyer import main as buyer
from seller import main as seller
from currency_reporter import main as chart_reporter


def main():
    print("Manager ON")


if __name__ == "__main__":
    main()
    wallet.main()
    buyer.main()
    seller.main()
    chart_reporter.main()
