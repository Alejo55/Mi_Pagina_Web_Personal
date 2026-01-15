import reflex as rx
import os

# Obtener la URL del backend desde variable de entorno
# Si API_URL no está definida, usar la URL de Railway (producción)
# Para desarrollo local, definir API_URL=http://localhost:8000
backend_url = os.getenv(
    "API_URL",
    "https://alejoagasiweb.up.railway.app"  # URL de producción por defecto
)

config = rx.Config(
    app_name="python_web",
    # URL del backend para que el frontend sepa dónde conectarse
    # Esta configuración se usa cuando se ejecuta 'reflex export'
    backend_url=backend_url,
    # Lista de dominios que pueden interactuar con tu backend
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://mi-pagina-web-personal.vercel.app",
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),  # Mejor para el diseño actual
    ],
    show_built_with_reflex=
    False,  # Para que se vea más profesional (sin el logo de Reflex)
)
