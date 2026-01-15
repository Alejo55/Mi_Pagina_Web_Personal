import reflex as rx

config = rx.Config(
    app_name="python_web",
    # Lista de dominios que pueden interactuar con tu backend
    # cors_allowed_origins=["*"],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
