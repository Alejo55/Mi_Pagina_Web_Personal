import reflex as rx

config = rx.Config(
    app_name="python_web",
    # FORZAMOS LA API URL AQUÍ
    api_url="https://289c1fc7-fb0e-4c12-8471-4106c46a6d05.fly.dev",
    # Lista de dominios que pueden interactuar con tu backend
    cors_allowed_origins=["*"],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
