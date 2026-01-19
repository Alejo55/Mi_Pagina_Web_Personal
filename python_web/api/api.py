import python_web.constants as const
from fastapi import FastAPI
from .TwitchAPI import TwitchAPI

fastapi_app = FastAPI()

# No tendria sentido regenerar api a cada rato (un nuevo token por cada persona que se conecta NO)
# Por eso inicializo instancia de API X para que sea comun
TWITCH_API = TwitchAPI()


@fastapi_app.get("/repo")
async def repo() -> str:
    return const.REPO_URL


@fastapi_app.get("/live/{user}")
async def live(user: str) -> bool:
    return TWITCH_API.live(user)
