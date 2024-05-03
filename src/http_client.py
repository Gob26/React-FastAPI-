from aiohttp import ClientSession

from src.config import settings


class HTTPClient:  #базовый объект для http запросов от него будем отталкиваться
    def __init__(self, base_url: str, api_key: str): #сессию не принимаем, а создаем внутри
        self.base_url = ClientSession(
            base_url=base_url,
            headers={"X-CMC_PRO_API_KEY": api_key   #добавляем хедер с ключом смотрим документацию на сайте с апи
                     }
        )


class CMCClient(HTTPClient):  #наследуемся от базового class HTTPClient
    async def get_listings(self):  #получаем список криптовалют с сайта CMC
        async with self.base_url.get(
                "/v1/cryptocurrency/listings/latest"
        ) as resp: # ссылку берем из документации
            return await resp.json()      #возвращаем в виде словаря
            return result["data"]  # получаем словарь данных по криптовалютам data это поле в словаре

    async def get_currency(self, currency_id:int):  #получаем конкретную криптовалюту по id
        async with self.base_url.get(
                "/v2/cryptocurrency/quotes/latest", # на сайте в документации
            params = {"id": currency_id} #передаем параметр id
        ) as resp: # ссылку берем из документации
            return await resp.json()      #возвращаем в виде словаря
            return result["data"][str(currency_id)]


