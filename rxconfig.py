import reflex as rx
import os

# Obtener la URL del backend desde variable de entorno
# Según la documentación de Reflex: https://reflex.dev/docs/hosting/self-hosting
# Se puede usar API_URL en tiempo de exportación para sobrescribir el valor por defecto
# Para desarrollo local, el valor por defecto es http://localhost:8000
api_url = os.getenv(
    "API_URL",
    "https://alejoagasiweb.up.railway.app"  # URL de producción por defecto
)

config = rx.Config(
    app_name="python_web",
    # api_url: URL del backend accesible públicamente
    # Según la documentación, esto es esencial para que el frontend interactúe con el backend
    # Se puede sobrescribir con la variable de entorno API_URL en tiempo de exportación
    api_url=api_url,
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
