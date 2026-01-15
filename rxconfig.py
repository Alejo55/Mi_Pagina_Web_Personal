import reflex as rx

config = rx.Config(
    app_name="python_web",
    # Lista de dominios que pueden interactuar con tu backend
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://mi-pagina-web-personal.vercel.app",
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),  # Mejor para el diseño actual
    ],
    show_built_with_reflex=False,  # Para que se vea más profesional (sin el logo de Reflex)
)
