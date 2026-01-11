import reflex as rx
import python_web.styles.styles as styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="5",
        style=styles.title_style,
    )
