import reflex as rx


# Común
def lang() -> rx.Component:  # Indica el idioma del documento
    return rx.script("document.documentElement.lang='es'")


preview = "/https://mi-pagina-web-personal.vercel.app/a-solid-full.png"  # Lo uso para Imagen de preview / metadata

__meta = [  # Privado
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
]


# Index
index_title = "Alejo Agasi | Software Engineer"
index_description = "Diseñando y desarrollando software de alto impacto."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(__meta)


# Certificates
certificates_title = "Alejo Agasi | Certificaciones"
certificates_description = (
    "Acreditaciones oficiales que validan mis competencias técnicas"
)

certificates_meta = [
    {"name": "og:title", "content": certificates_title},
    {"name": "og:description", "content": certificates_description},
]
certificates_meta.extend(__meta)
