class Operation:
    def __init__(self, date, currency_bought, amount_bought, currency_paid, amount_paid):
        self._date = date
        self._currency_bought = currency_bought
        self._amount_bought = amount_bought
        self._currency_paid = currency_paid
        self._amount_paid = amount_paid

    def get_info(self):
        return {
            "date": self._date,
            "bought": {
                "currency": self._currency_bought,
                "amount": self._amount_bought
            },
            "paid": {
                "currency": self._currency_paid,
                "amount": self._amount_paid
            }
        }
