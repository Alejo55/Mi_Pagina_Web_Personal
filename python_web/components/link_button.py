import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size


def link_button(
    title: str, body: str, image: str, url: str, is_external=True, highlight_color=None
) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.BIG.value,
                    height="auto",
                    margin=Size.MEDIUM.value,
                    alt=title,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",  # Texto alineado a la izquierda entre sí
                    spacing="0",  # Elimina espacio extra entre líneas de texto
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                width="100%",
                align="center",
            ),
            border_style="solid",
            border_color=highlight_color,
            border_width="2px" if highlight_color != None else None,
        ),
        href=url,
        is_external=is_external,
        width="100%",
    )
