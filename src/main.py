import fastapi as FastAPI

from src.config import settings
from src.http_client import CMCClient

app = FastAPI()


cmc_client = CMCClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)

@app.get("/cryptocurrencies")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()


@app.get("/cryptocurrency/{currency_id}")
async def get_currency(currency_id: int):
    return await cmc_client.get_currency(currency_id)