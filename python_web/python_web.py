import reflex as rx
import python_web.styles.styles as styles

# Importar las paginas igual aunque no lo use porque puede dar error
from python_web.pages.index import index
from python_web.pages.certificates import certificates


# Manejaremos estados programados y ejecutados en python, por lo que hay que desplegar
# el proyecto en un servidor no solo estatico sino tambien que corra python.
# State para Backend
class State(rx.State):
    """
    Docstring for State
    """


# app es un componente de Reflex que representa la aplicacion web
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    head_components=[
        rx.el.link(
            rel="icon",
            href="/a-solid-full.png",  # Favicon del navegador
            type="image/png",
        ),
    ],
)

# Luego en terminal, correr: reflex run
