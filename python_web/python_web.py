import reflex as rx
from python_web.components.navbar import navbar
from python_web.views.header import header
from python_web.views.links import links
from python_web.components.footer import footer
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size


# # Clase State encargada de manejar el estado de la aplicacion (ej. un click)
# class State(rx.State):
#     pass


# Pagina inicial = index
# Devuelvo un componente, que representa la parte grafica
# Por debajo, los componentes de Reflex utilizan componentes de React
# En concreto, desde la versión 0.4.0, Reflex utiliza Radix (en vez de Chakra)
# El componente puede tener propiedades propias como tambien de CSS (importante usar snake_case)
def index() -> rx.Component:
    # Box es un contenedor generico que agrupa otros componentes
    return rx.box(
        navbar(),
        # El componente rx.center centra el "bloque" (la columna),
        # pero no dicta cómo se alinean las cosas dentro de ese bloque.
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                spacing="5",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.BIG.value,
                margin_y=Size.BIG.value,
                align="center",  # <--- CRUCIAL: Centra el header y los links dentro de la columna
            ),
        ),
        footer(),
    )


# app es un componente de Reflex que representa la aplicacion web
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    head_components=[
        rx.el.link(
            rel="icon",
            href="/a-solid-full.png",
            type="image/png",
        ),
    ],
)

# Agrego la pagina index a la app
app.add_page(
    index,
    title="Alejo Agasi | Software Engineer",
    description="Diseñando y desarrollando software de alto impacto.",
    # Usar la ruta absoluta aquí también ayuda a los navegadores
    image="/a-solid-full.png",
)
# Compilo la app
app._compile()
# Luego en terminal, correr: reflex run
