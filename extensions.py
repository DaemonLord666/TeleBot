import currencyapicom
from config import keys
client = currencyapicom.Client('cur_live_jwLrg2DNIwkERQiHmpMIHJOB8YNesSOkSjCZ8HO0')

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote:str, base:str, amount:str):
        
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
    
    
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {quote}')
    
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {base}')
    
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'не удалось обработать количество {amount}')
        
        result = client.latest(quote_ticker,currencies=[base_ticker])
        result = result['data'][base_ticker]['value']
        result = float (result) * amount
        return result
