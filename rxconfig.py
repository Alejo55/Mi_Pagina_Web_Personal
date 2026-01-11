import reflex as rx

config = rx.Config(
    app_name="python_web",
    # Lista de dominios que pueden interactuar con tu backend
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://mi-pagina-web-personal.vercel.app",  # Reemplaza con tu URL real de Vercel
        "https://python-web-cyan-sun.reflex.run",
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
