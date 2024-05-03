import fastapi
from src.router import router as router_crypto
from src.config import settings
from src.http_client import CMCClient

app = fastapi.FastAPI()

app.include_router(router_crypto) #добавляем роутер криптовалют

