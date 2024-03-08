import reflex as rx

from portafolio_personal.components.heading import heading
from portafolio_personal.components.media import media
from portafolio_personal.data import Data
from portafolio_personal.styles.styles import Size
from portafolio_personal.translations import get_translation

def  header(data: Data, lang) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=data.avatar,
            size=Size.LARGE.value
        ),
        rx.vstack(
            heading(data.name, True),
            heading(data.job_position),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit",
            ),
            media(data.media),
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )