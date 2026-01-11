import reflex as rx
from python_web.components.link_button import link_button
from python_web.components.title import title
import python_web.constants as const


def links() -> rx.Component:
    return rx.vstack(
        title("Mis Redes Sociales"),
        link_button(
            "LinkedIn",
            "Mira mi perfil profesional",
            "icons/linkedin_icon.svg",
            const.LINKEDIN_URL,
        ),
        link_button(
            "GitHub",
            "Mira mis repositorios",
            "icons/github_icon.svg",
            const.GITHUB_URL,
        ),
        link_button(
            "Instagram",
            "Mira mis fotos",
            "icons/instagram_icon.svg",
            const.INSTAGRAM_URL,
        ),
        title("Contacto"),
        link_button(
            "Email", const.EMAIL, "icons/email_icon.svg", f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing="3",
    )
