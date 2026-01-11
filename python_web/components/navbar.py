import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size
from python_web.styles.colors import Color as Color


# Devuelvo un contenedor horizontal (hstack) que hara de navbar (Barra de navegacion)
def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("Alejo", as_="span", color=Color.PRIMARY.value),
            rx.text("Agasi", as_="span", color=Color.SECONDARY.value),
            style=styles.navbar_title_style,
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
