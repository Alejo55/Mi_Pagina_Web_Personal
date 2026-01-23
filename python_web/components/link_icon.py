import reflex as rx
from python_web.styles.styles import Size


def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.EXTRA_LARGE.value,
            height=Size.EXTRA_LARGE.value,
            alt=alt,
        ),
        href=url,
        is_external=True,
    )
