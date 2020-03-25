"""
Handle funds.csv, read and write values for each currency
"""
import csv


def get_funds_from_file():
    funds_data = []
    with open("funds.csv", mode="r") as funds_file:
        funds = csv.DictReader(funds_file)
        for row in funds:
            funds_data.append(row)
    return funds_data


def get_funds_from_raw(funds_data):
    """
    Set dictionary with currency-key and its funds as value, from csv input
    """
    funds = {}
    for currency in funds_data:
        funds[currency["name"]] = currency["amount"]
    return funds


def get_funds():
    """
    Entry-point - Read funds from file and process them
    """
    print("[WALLET] - Reading funds from file")
    raw_data = get_funds_from_file()
    return get_funds_from_raw(raw_data)
