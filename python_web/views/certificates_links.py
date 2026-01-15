import reflex as rx
from python_web.components.link_button import link_button
from python_web.components.title import title
import python_web.constants as const


def certificates_links() -> rx.Component:
    return rx.vstack(
        title("Mis Certificaciones"),
        link_button(
            "Microsoft Certified: Azure Data Fundamentals",
            "Conceptos de datos relacionales, NoSQL y analítica en la nube",
            "/icons/email_icon.svg",
            const.AZURE_DATA_CERT,
        ),
        link_button(
            "Microsoft Certified: Azure Fundamentals",
            "Arquitectura cloud, servicios clave y gobernanza en Azure",
            "/icons/email_icon.svg",
            const.AZURE_CLOUD_CERT,
        ),
        link_button(
            "Python Programming",
            "Dominio de sintaxis, estructuras de datos y lógica algorítmica",
            "/icons/email_icon.svg",
            const.SANTANDER_PYTHON_CERT,
        ),
        link_button(
            "Python and Cursor: Smarter Development with AI",
            "Codificación ágil asistida por IA para optimizar flujos de trabajo",
            "/icons/email_icon.svg",
            const.SANTANDER_PYTHON_CURSOR_CERT,
        ),
        link_button(
            "Postman API Fundamentals Student Expert",
            "Envío de peticiones, validación y documentación de APIs",
            "/icons/email_icon.svg",
            const.POSTMAN_CERT,
        ),
        width="100%",
        spacing="3",
    )
