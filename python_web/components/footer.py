import reflex as rx
import datetime
from python_web.styles.styles import Size
from python_web.styles.colors import TextColor as TextColor
from python_web.styles.colors import Color as Color
import python_web.constants as const


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height=Size.VERY_BIG.value,
            width="auto",
            padding="2px",
            bg=Color.SECONDARY.value,
            alt="Logotipo de Alejo Agasi, Ingeniero de Software",
        ),
        rx.link(
            f"Alejo Agasi © {datetime.datetime.now().year}",
            href=const.LINKEDIN_URL,
            is_external=True,
            font_size=Size.MEDIUM.value,
            margin_top=Size.MEDIUM.value,
        ),
        rx.text("All rights reserved.", font_size=Size.MEDIUM.value),
        spacing="0",
        align="center",  # <--- Centra los elementos del footer
        width="100%",
        margin_bottom=Size.BIG.value,  # Un poco de espacio abajo queda mejor
        padding_bottom=Size.BIG.value,  # Un poco de espacio abajo queda mejor
        color=TextColor.FOOTER.value,
    )
