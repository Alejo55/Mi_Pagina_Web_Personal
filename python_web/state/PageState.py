# Manejaremos estados programados y ejecutados en python, por lo que hay que desplegar
# el proyecto en un servidor no solo estatico sino tambien que corra python.
# State para Backend. Es algo que variará.

import reflex as rx
import python_web.constants as const
from python_web.api.api import live


class PageState(rx.State):

    is_live: bool = False

    # Antes @rx.var -> Para estados que se estan calculando en caliente, en tiempo de ejecucion,
    # y sin llamar al backend (no llama a servidor externo)
    # Pero ahora es async porque habra un server externo -> Llama a API.

    @rx.event
    async def check_live(self):  # Self para acceder al contexto.
        # await para esperar a que responda ya que es una operacion asincrona
        self.is_live = await live(const.USER_TWITCH)
