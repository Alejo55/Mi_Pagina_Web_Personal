import reflex as rx
import python_web.constants as const
from python_web.components.link_button import link_button
from python_web.components.title import title
from python_web.styles.colors import Color
from python_web.state.PageState import PageState


def certificates_links() -> rx.Component:
    return rx.vstack(
        rx.cond(
            PageState.cert_info,
            rx.vstack(
                title("Mis Certificaciones"),
                rx.foreach(
                    PageState.cert_info,
                    lambda item: link_button(
                        item["title"],
                        item["body"],
                        item["url_icon"],
                        item["url_pdf"],
                        highlight_color=Color.SECONDARY.value,
                    ),
                ),
                width="100%",
                spacing="3",
            ),
        ),
        width="100%",
        on_mount=PageState.cert_links,
    )
