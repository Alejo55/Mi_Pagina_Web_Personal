# https://ant.design/
# Es otra libreria de componentes de React como Radix o Chakra

import reflex as rx
from python_web.styles.colors import Color as Color


# Boton flotante que aparecera siempre abajo a la derecha, por lo que da igual donde lo coloquemos
class FloatButton(rx.Component):
    # Para usar componente de React desde Reflex, usamos dos propiedades:
    library = "antd"  # Librería que queremos utilizar
    tag = "FloatButton"  # Elemento que importo

    # IMPORTANTE ESPECIFICAR EL TIPO DE LOS SIGUIENTES PARA QUE FUNCIONE
    icon: rx.Var[rx.Component]  # Elemento variable, que lo podre pasar por argumento
    href: rx.Var[str]  # Elemento variable, que lo podre pasar por argumento
    target: rx.Var[str] = "_blank"  # Nueva pestaña
    badge: rx.Var[dict] = {
        "dot": True,
        "color": Color.SECONDARY.value,
        "offset": [4, -3],
    }  # Para configurar lo relativo al aviso


# Todo componente tiene una operacion que permite crear el componente
# Esto permitira importar el boton ya creado
float_button = FloatButton.create
