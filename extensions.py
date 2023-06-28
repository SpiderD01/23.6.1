import requests
import json
from config import keys

class APIException(Exception):
    pass

class CurseConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Неподдерживаемая валюта {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Неподдерживаемая валюта {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не корректно введено количество валюты: {amount}")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = (json.loads(r.content)[keys[base]])
        return (total_base)