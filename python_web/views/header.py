import reflex as rx
import python_web.constants as const
import python_web.styles.styles as styles
from python_web.styles.colors import TextColor
from python_web.styles.colors import Color
from python_web.components.link_icon import link_icon
from python_web.components.info_text import info_text
from python_web.styles.styles import Size, Spacing
from python_web.state.PageState import PageState
from python_web.components.link_button import link_button


def header(details: bool = True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.cond(
                    PageState.live_status.live,
                    rx.link(
                        rx.image(
                            src="/icons/twitch_icon.svg",
                            height=Size.DEFAULT.value,
                            width=Size.DEFAULT.value,
                        ),
                        href=const.TWITCH_URL,
                        is_external=True,
                        class_name="blink",
                        border_radius="50%",
                        padding=Size.SMALL.value,
                        bg=Color.PURPLE.value,
                        position="absolute",
                        top=f"-{Size.SMALL.value}",
                        right=f"-{Size.SMALL.value}",
                        z_index="2",
                    ),
                ),
                rx.avatar(
                    name="Alejo Agasi",
                    size=Spacing.MEDIUM_BIG.value,  # Subí a 7 para que el borde luzca mejor
                    src="/foto_mia.jpg",  # Recuerda el "/" inicial si está en assets
                    fallback="AA",  # Esto fuerza a que aparezcan las letras si no hay foto
                    radius="none",
                    color=TextColor.HEADER.value,
                    bg=Color.SECONDARY.value,
                    style=styles.image_style,
                    alt="Avatar Alejo Agasi",
                    # # Truco del borde:
                    # # Usamos padding para que el fondo (bg) se vea como un borde
                    # padding=Size.VERY_SMALL.value,
                ),
                position="relative",
            ),
            rx.vstack(
                rx.vstack(
                    rx.heading("Alejo Agasi", size=Spacing.LARGE.value),
                    rx.heading(
                        "Ingeniero Informático",
                        size=Spacing.DEFAULT.value,
                        color=Color.SECONDARY.value,
                    ),
                    spacing=Spacing.ZERO.value,
                    align_items="start",
                ),
                rx.hstack(
                    link_icon("/icons/github_icon.svg", const.GITHUB_URL, "GitHub"),
                    link_icon(
                        "/icons/linkedin_icon.svg", const.LINKEDIN_URL, "LinkedIn"
                    ),
                    spacing=Spacing.BIG.value,  # Espacio entre los iconos
                ),
                spacing=Spacing.MEDIUM_SMALL.value,  # Este es el espacio que habrá entre el bloque de texto y los links
                align_items="start",
            ),
            align_items="center",
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text("Estudiante avanzado", "en la UNLaM"),
                    rx.spacer(),
                    info_text("Stack técnico", "en Python, Java, SQL y C/C++"),
                    rx.spacer(),
                    info_text(
                        f"{PageState.cert_info.length()}",
                        "certificaciones oficiales",
                    ),
                    width="100%",
                    # Opcional: añade un gap mínimo por si el spacer se queda sin espacio
                    spacing=Spacing.DEFAULT.value,
                ),
                rx.cond(
                    PageState.live_status.live,
                    link_button(
                        "En directo",
                        PageState.live_status.title,
                        "/icons/twitch_icon.svg",
                        const.TWITCH_URL,
                        highlight_color=Color.PURPLE.value,
                        animation=styles.ZOOMINLEFT_ANIMATION,
                    ),
                ),
                rx.text(
                    """
                    Técnico Universitario en Desarrollo de Software y estudiante avanzado de Ingeniería Informática. 
                    Cuento con experiencia en ingeniería de datos, back-end y bases de datos relacionales. 
                    Me apasiona construir soluciones escalables y aprender nuevas tecnologías para resolver problemas complejos de software.
                    """,
                    text_align="start",
                    color=TextColor.BODY.value,
                ),
                spacing=Spacing.BIG.value,
                width="100%",
            ),
        ),
        align_items="start",
        spacing=Spacing.BIG.value,
        width="100%",  # <--- Asegura que ocupe todo el ancho disponible
        # The on_mount event handler is called after the component is rendered on the page.
        # It is similar to a page on_load event, although it does not necessarily fire when navigating between pages.
        on_mount=[PageState.check_live, PageState.cert_links],
    )
