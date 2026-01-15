import reflex as rx
import python_web.styles.styles as styles
import python_web.constants as const
from python_web.styles.styles import Size as Size
from python_web.styles.colors import Color as Color
from python_web.routes import Route as Route
from python_web.components.ant_components import float_button


# Devuelvo un contenedor horizontal (hstack) que hara de navbar (Barra de navegacion)
def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("Alejo", as_="span", color=Color.PRIMARY.value),
                rx.text("Agasi", as_="span", color=Color.SECONDARY.value),
                style=styles.navbar_title_style,
            ),
            href=Route.INDEX.value,
        ),
        float_button(
            icon=rx.image(
                src="/icons/linkedin_dark_icon.svg",
                width=Size.BIG.value,  # ¡OBLIGATORIO!
                height=Size.BIG.value,  # ¡OBLIGATORIO!
            ),
            href=const.LINKEDIN_URL,
        ),
        # Posicion fija para que se mantenga al hacer scroll
        position="sticky",
        bg=Color.CONTENT.value,
        # Padding horizontal y vertical. Independiente del texto
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        # z-index alto para que este por encima de otros elementos
        z_index="999",
        # Top 0 para que se quede en la parte superior
        top="0",
    )
