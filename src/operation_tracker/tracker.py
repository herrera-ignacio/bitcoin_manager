"""
Handle operations.csv, read and write operations information

What am I interested to know?
* Last operation (what did I buy, ARS or BTC?)
"""
import csv


class Tracker:
    def __init__(self):
        print("[TRACKER] OK")
        self._operations_file = "operations.csv"
        self._operations = []
        self.load_operations_from_file()

    def register_operation(self, operation):
        self._operations.append(operation)

    def load_operations_from_file(self):
        with open("operations.csv", mode="r") as operations_file:
            operations = csv.DictReader(operations_file)
            for operation in operations:
                self.register_operation(operation)
        print("[TRACKER] - Operations loaded")

    def get_last_operation(self):
        return self._operations[-1]

    def get_last_buy(self):
        last_operation = self.get_last_operation()
        return {
            "currency": last_operation["currency_bought"],
            "amount": last_operation["amount_bought"]
        }
