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
        rx.text(
            f"© 2019-{datetime.datetime.now().year} Alejo Agasi",
            font_size=Size.MEDIUM.value,
            margin_top=Size.MEDIUM.value,
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github_icon.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Logo GitHub",
                ),
                rx.vstack(
                    rx.text(
                        "Ver código fuente del proyecto",
                        font_size=Size.MEDIUM.value,
                    ),
                    rx.text(
                        "Construido con Python y Reflex", font_size=Size.MEDIUM.value
                    ),
                    spacing=Spacing.VERY_SMALL.value,
                    align_items="start",
                ),
                align_items="center",
                spacing=Spacing.SMALL.value,
            ),
            href=const.REPO_URL,
            is_external=True,
            color=TextColor.FOOTER.value,
            padding_top=Size.DEFAULT.value,
        ),
        spacing=Spacing.ZERO.value,
        align="center",  # <--- Centra los elementos del footer
        width="100%",
        margin_bottom=Size.BIG.value,  # Un poco de espacio abajo queda mejor
        padding_bottom=Size.BIG.value,  # Un poco de espacio abajo queda mejor
        color=TextColor.FOOTER.value,
    )
