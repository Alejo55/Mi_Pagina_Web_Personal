from enum import Enum


class Color(Enum):
    # Principal del logotipo
    PRIMARY = "#7495D6"

    # Secundario del logotipo
    SECONDARY = "#14B8A6"

    # El fondo general de la app
    BACKGROUND = "#0D1117"

    CONTENT = "#1F2937"

    PURPLE = "#9146ff"

    GOLD = "#D3A745"


class TextColor(Enum):
    # Blanco puro o muy brillante
    HEADER = "#F3F4F6"

    # Gris claro azulado para que no canse la vista al leer
    BODY = "#C9D1D9"

    # Gris medio
    FOOTER = "#8B949E"
