import reflex as rx

from portafolio_personal.components.heading import heading
from portafolio_personal.components.media import media
from portafolio_personal.data import Data
from portafolio_personal.styles.styles import Size

def  header(data: Data) -> rx.Component:
    return rx.flex(
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
            spacing=Size.DEFAULT.value
        ),
        spacing=Size.DEFAULT.value,
        flex_direction=["column ", "row"],
        align_items="center",
    )