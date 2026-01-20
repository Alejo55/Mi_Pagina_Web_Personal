import reflex as rx
import python_web.constants as const
from python_web.components.link_button import link_button
from python_web.components.title import title
from python_web.styles.colors import Color
from python_web.state.PageState import PageState


def certificates_links() -> rx.Component:
    # return rx.cond(
    #     len(PageState.cert_info) > 0,
    #     rx.vstack(
    #         title("Mis Certificaciones"),
    #         rx.foreach(
    #             PageState.cert_info,
    #             lambda item: link_button(
    #                 item["title"],
    #                 "blablabla",
    #                 "/icons/email_icon.svg",
    #                 item["url"],
    #                 highlight_color=Color.SECONDARY.value,
    #             ),
    #         ),
    #     ),
    #     width="100%",
    #     spacing="3",
    #     on_mount=PageState.cert_links,
    # )

    return rx.vstack(
        title("Mis Certificaciones"),
        link_button(
            "Microsoft Certified: Azure Data Fundamentals",
            "Conceptos de datos relacionales, NoSQL y analítica en la nube",
            "/icons/email_icon.svg",
            const.AZURE_DATA_CERT,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "Microsoft Certified: Azure Fundamentals",
            "Arquitectura cloud, servicios clave y gobernanza en Azure",
            "/icons/email_icon.svg",
            const.AZURE_CLOUD_CERT,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "Python Programming",
            "Dominio de sintaxis, estructuras de datos y lógica algorítmica",
            "/icons/email_icon.svg",
            const.SANTANDER_PYTHON_CERT,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "Python and Cursor: Smarter Development with AI",
            "Codificación ágil asistida por IA para optimizar flujos de trabajo",
            "/icons/email_icon.svg",
            const.SANTANDER_PYTHON_CURSOR_CERT,
            highlight_color=Color.SECONDARY.value,
        ),
        link_button(
            "Postman API Fundamentals Student Expert",
            "Envío de peticiones, validación y documentación de APIs",
            "/icons/email_icon.svg",
            const.POSTMAN_CERT,
            highlight_color=Color.SECONDARY.value,
        ),
        width="100%",
        spacing="3",
        # on_mount=PageState.cert_links,
    )
