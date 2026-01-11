import reflex as rx
from python_web.styles.colors import TextColor as TextColor
from python_web.styles.colors import Color as Color
from python_web.components.link_icon import link_icon
from python_web.components.info_text import info_text
import python_web.constants as const
import datetime

from python_web.styles.styles import Size


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Alejo Agasi",
                size="7",  # Subí a 7 para que el borde luzca mejor
                src="/foto_mia.jpg",  # Recuerda el "/" inicial si está en assets
                fallback="AA",  # Esto fuerza a que aparezcan las letras si no hay foto
                # Esto asegura que sea un círculo perfecto
                radius="full",
                # Truco del borde:
                # Usamos padding para que el fondo (bg) se vea como un borde
                padding="2px",
                bg=Color.SECONDARY.value,
            ),
            rx.vstack(
                rx.vstack(
                    rx.heading("Alejo Agasi", size="5"),
                    rx.text("@yo", color=Color.SECONDARY.value),
                    spacing="0",
                    align_items="start",
                ),
                rx.hstack(
                    link_icon(
                        "icons/linkedin_icon.svg", const.LINKEDIN_URL, "LinkedIn"
                    ),
                    link_icon(
                        "icons/linkedin_icon.svg", const.LINKEDIN_URL, "LinkedIn"
                    ),
                    link_icon(
                        "icons/linkedin_icon.svg", const.LINKEDIN_URL, "LinkedIn"
                    ),
                    spacing="5",  # Espacio entre los iconos
                ),
                spacing="2",  # Este es el espacio que habrá entre el bloque de texto y los links
                align_items="start",
            ),
            align_items="center",
        ),
        rx.flex(
            info_text(f"{años_estudios()}+", "años sumando conocimientos informáticos"),
            rx.spacer(),
            info_text(f"{años_estudios()}+", "años sumando conocimientos informáticos"),
            rx.spacer(),
            info_text(f"{años_estudios()}+", "años sumando conocimientos informáticos"),
            width="100%",
            padding_x=Size.MEDIUM.value,  # <--- Añade espacio a los lados
            # Opcional: añade un gap mínimo por si el spacer se queda sin espacio
            spacing="4",
        ),
        rx.text(
            """
        Técnico Universitario en Desarrollo de Software y estudiante avanzado de Ingeniería Informática, 
        con experiencia como Data Engineer Trainee, donde adquirí bases prácticas en ingesta, transformación 
        y análisis de datos dentro de un entorno profesional.
        """,
            text_align="center",
            color=TextColor.BODY.value,
        ),
        align_items="center",
        spacing="6",
        width="100%",  # <--- Asegura que ocupe todo el ancho disponible
    )


def años_estudios() -> int:
    return datetime.datetime.now().year - 2019
