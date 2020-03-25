from abc import ABC, abstractmethod
from typing import Dict


class Provider(ABC):
    def __init__(self, name: str, currencies: Dict[str, any]):
        self._name = name
        self._currencies = currencies

    @abstractmethod
    def get_rates(self, from_currency: str, to_currency: str):
        pass
