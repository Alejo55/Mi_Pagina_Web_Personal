import reflex as rx
import python_web.constants as const
from python_web.components.link_button import link_button
from python_web.components.title import title
from python_web.routes import Route
from python_web.styles.colors import Color
from python_web.styles.styles import Spacing


def index_links() -> rx.Component:
    return rx.vstack(
        title("Certificaciones Técnicas"),
        link_button(
            "Mis certificaciones",
            "Historial de especializaciones y credenciales técnicas",
            "/icons/cert_icon.svg",
            Route.CERTIFICATES.value,
            is_external=False,
            highlight_color=Color.GOLD.value,
        ),
        title("Más Sobre Mí"),
        link_button(
            "Instagram",
            "Mi día a día fuera de la oficina",
            "/icons/instagram_icon.svg",
            const.INSTAGRAM_URL,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "Twitter (X)",
            "Opiniones y actualidad",
            "/icons/x_icon.svg",
            const.X_URL,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "Discord",
            "Comunidades y amigos",
            "/icons/discord_icon.svg",
            const.DISCORD_URL,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "Twitch",
            "Directos y ocio",
            "/icons/twitch_icon.svg",
            const.TWITCH_URL,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "YouTube",
            "Lo que veo en mi tiempo libre",
            "/icons/youtube_icon.svg",
            const.YOUTUBE_URL,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "TikTok",
            "Entretenimiento y tendencias",
            "/icons/tiktok_icon.svg",
            const.TIKTOK_URL,
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
