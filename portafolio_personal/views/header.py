import reflex as rx

from portafolio_personal.components.heading import heading
from portafolio_personal.components.media import media
from portafolio_personal.styles.styles import Size

def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(size=Size.LARGE.value),
        rx.vstack(
            heading("Nombre Apellido", True),
            heading("Desarrollador de Software"),
            rx.text(
                rx.icon("map-pin"),
                "Localización",
                display="inherit",
            ),
            media(),
            spacing=Size.SMALL.value

        ),
        spacing=Size.DEFAULT.value
    )