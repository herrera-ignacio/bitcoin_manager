"""
Handle operations.csv, read and write operations information

What am I interested to know?
* Last operation (what did I buy, ARS or BTC?)
* 
"""
import csv


def get_operations_from_file():
    raw_operations = []
    with open("operations.csv", mode="r") as operations_file:
        funds = csv.DictReader(operations_file)
        for row in funds:
            raw_operations.append(row)
    return raw_operations

