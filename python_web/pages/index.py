import reflex as rx
import python_web.styles.styles as styles
import python_web.utils as utils
from python_web.components.navbar import navbar
from python_web.views.header import header
from python_web.views.index_links import index_links
from python_web.components.footer import footer
from python_web.styles.styles import Size as Size


# Pagina inicial = index
# Devuelvo un componente, que representa la parte grafica
# Por debajo, los componentes de Reflex utilizan componentes de React
# En concreto, desde la versión 0.4.0, Reflex utiliza Radix (en vez de Chakra)
# El componente puede tener propiedades propias como tambien de CSS (importante usar snake_case)
@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
)
# Lo que esta a continuacion sera una pagina
# index por defecto sera la raiz SIEMPRE, por eso no es necesario especificarle la ruta
def index() -> rx.Component:
    # Box es un contenedor generico que agrupa otros componentes
    return rx.box(
        utils.lang(),
        navbar(),
        # El componente rx.center centra el "bloque" (la columna),
        # pero no dicta cómo se alinean las cosas dentro de ese bloque.
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                spacing="5",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.BIG.value,
                margin_y=Size.BIG.value,
                align="center",  # <--- CRUCIAL: Centra el header y los links dentro de la columna
            ),
        ),
        footer(),
    )
