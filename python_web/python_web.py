import reflex as rx
import python_web.styles.styles as styles
from python_web.api.api import fastapi_app

# Importar las paginas igual aunque no lo use porque puede dar error
from python_web.pages.index import index
from python_web.pages.certificates import certificates


# app es un componente de Reflex que representa la aplicacion web
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    api_transformer=fastapi_app,
    head_components=[
        rx.el.link(
            rel="icon",
            href="/a-solid-full.png",  # Favicon del navegador
            type="image/png",
        ),
    ],
)
