import reflex as rx
import datetime
import python_web.constants as const
from python_web.styles.styles import Size, Spacing
from python_web.styles.colors import TextColor
from python_web.styles.colors import Color


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height=Size.VERY_BIG.value,
            width="auto",
            padding=Size.VERY_SMALL.value,
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
        spacing=Spacing.ZERO.value,
        align="center",  # <--- Centra los elementos del footer
        width="100%",
        margin_bottom=Size.BIG.value,  # Un poco de espacio abajo queda mejor
        padding_bottom=Size.BIG.value,  # Un poco de espacio abajo queda mejor
        color=TextColor.FOOTER.value,
    )
