import reflex as rx
from python_web.styles.styles import Size
from python_web.styles.colors import TextColor
from python_web.styles.colors import Color


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title, as_="span", font_weight="bold", color=Color.SECONDARY.value),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value,
        text_align="center",
    )
