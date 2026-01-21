import reflex as rx
import python_web.constants as const
from python_web.components.link_button import link_button
from python_web.components.title import title
from python_web.routes import Route
from python_web.styles.colors import Color
from python_web.styles.styles import Spacing


def index_links() -> rx.Component:
    return rx.vstack(
        title("Mis Redes Sociales"),
        link_button(
            "Mis certificaciones",
            "Historial de especializaciones y credenciales técnicas",
            "/icons/email_icon.svg",
            Route.CERTIFICATES.value,
            is_external=False,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "LinkedIn",
            "Mira mi perfil profesional",
            "/icons/linkedin_icon.svg",
            const.LINKEDIN_URL,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "GitHub",
            "Mira mis repositorios",
            "/icons/github_icon.svg",
            const.GITHUB_URL,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "Instagram",
            "Mira mis fotos",
            "/icons/instagram_icon.svg",
            const.INSTAGRAM_URL,
            highlight_color=Color.SECONDARY.value,
        ),
        title("Contacto"),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email_icon.svg",
            f"mailto:{const.EMAIL}",
        ),
        width="100%",
        spacing=Spacing.SMALL.value,
    )
