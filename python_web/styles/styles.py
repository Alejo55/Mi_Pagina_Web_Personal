import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

# Constantes de estilos
MAX_WIDTH = "560px"

# Fuentes
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Audiowide&display=swap",
    "https://fonts.googleapis.com/css2?family=Zalando+Sans+Expanded:wght@400&display=swap",
    "https://fonts.googleapis.com/css2?family=Zalando+Sans:wght@400&display=swap",
    "/css/styles.css",
]


# Tamaños por defecto (encapsulados gracias a Enum)
class Size(Enum):
    # 1em = Tamaño de la fuente actual de la aplicación (16 px). Tamaño relativo.
    # Tamaño en em = Píxeles deseados / Tamaño de fuente del padre (o base)
    # Antes usaba px, pero es propenso a romperse en pantallas pequeñas o grandes
    VERY_SMALL = "0.125em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    MEDIUM_SMALL = "2"
    SMALL = "3"
    DEFAULT = "4"  # 16px / 1em
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"


# Estilos que afectan a toda la aplicación
# Las propiedades que no sean del elemento no se pueden meter en la hoja de estilos,
# deben meterse en el elemento directamente (ej. size)
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    "overflow_x": "hidden",  # Permite que si no hay espacio, no empuje el contenido fuera
    rx.text: {
        "white_space": "normal",
        "overflow_wrap": "break-word",  # Recomendado para que palabras largas (como un email) no rompan el layout
    },
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "white_space": "normal",
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",  # Si el texto es más largo que el ancho del botón, se dividirá en dos o más líneas automáticamente.
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value,
        },
    },
    rx.link: {"text_decoration": "none", "_hover": {}},
}


navbar_title_style = dict(font_family=Font.LOGO.value, font_size=Size.LARGE.value)


title_style = dict(
    width="100%",
    font_family=Font.TITLE.value,
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value,
)
