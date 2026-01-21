import reflex as rx
import python_web.styles.styles as styles
import python_web.utils as utils
from python_web.components.navbar import navbar
from python_web.views.header import header
from python_web.views.certificates_links import certificates_links
from python_web.components.footer import footer
from python_web.styles.styles import Size, Spacing
from python_web.routes import Route


@rx.page(
    route=Route.CERTIFICATES.value,
    title=utils.certificates_title,
    description=utils.certificates_description,
    image=utils.preview,
    meta=utils.certificates_meta,
)
def certificates() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                certificates_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                spacing=Spacing.LARGE.value,
                padding=Size.DEFAULT.value,
                margin_y=Size.BIG.value,
                align="center",
            ),
        ),
        footer(),
    )
