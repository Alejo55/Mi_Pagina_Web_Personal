import reflex as rx
from python_web.styles.styles import Size
from python_web.styles.colors import TextColor
from python_web.styles.colors import Color


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        # El título resaltado arriba
        rx.text(
            title,
            font_size=Size.MEDIUM.value,
            font_weight="bold",
            color=Color.SECONDARY.value,
        ),
        # El cuerpo debajo (salto de línea automático)
        rx.text(
            body,
            font_size=Size.MEDIUM.value,
            color=TextColor.BODY.value,
        ),
        text_align="center",  # Mantiene ambos textos centrados entre sí
    )
