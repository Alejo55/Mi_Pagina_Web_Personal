import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Spacing


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size=Spacing.LARGE.value,
        style=styles.title_style,
    )
