from providers.provider import Provider
from providers.ripio import RipioProvider
from time import sleep


class Reporter:
    """
    Responsible of fetching rates and logging reports
    """
    __reporter = None
    _providers = []

    @classmethod
    def get_reporter(cls):
        if cls.__reporter is None:
            cls()
        return cls.__reporter

    def __init__(self):
        print("[Reporter] Loading...")
        if self.__class__.__reporter is not None:
            raise Exception("[Reporter] Reporter loaded already!")
        else:
            self.__class__.__reporter = self

    def add_provider(self, provider: Provider):
        print("[Reporter] Adding provider...")
        self._providers.append(provider)

    def get_rates(self, from_currency: str, to_currency: str):
        # print(f"[Reporter] GET {from_currency}-{to_currency} rates")
        for provider in self._providers:
            print(provider.get_rates(from_currency, to_currency))

    def generate_reports(self, interval: int):
        while True:
            self.get_rates("BTC", "ARS")
            sleep(interval)

