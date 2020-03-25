import requests
from .provider import Provider


# Ripio updates rates every 1 min
class RipioProvider(Provider):
    def __init__(self):
        print("[PROVIDER:Ripio] OK")
        currencies = {
            "BTC": {
                "name": "bitcoin",
                "url": "https://ripio.com/api/v1/rates/",
            }
        }
        super().__init__("Ripio", currencies)

    def get_currency_rate_url(self, currency: str):
        return self._currencies[currency]["url"]

    @staticmethod
    def filter_rate_by_currency(rates, to_currency: str):
        buy_tag = f"{to_currency}_BUY"
        sell_tag = f"{to_currency}_SELL"
        return {
            buy_tag: rates[buy_tag],
            sell_tag: rates[sell_tag]
        }

    def get_rates(self, from_currency: str, to_currency: str):
        data = requests.get(self.get_currency_rate_url(from_currency))
        rates = RipioProvider.filter_rate_by_currency(data.json()["rates"], "ARS")
        return {from_currency: rates}
