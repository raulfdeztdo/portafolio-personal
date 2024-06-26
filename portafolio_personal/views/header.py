import reflex as rx

from portafolio_personal.components.heading import heading
from portafolio_personal.components.media import media
from portafolio_personal.data import Data
from portafolio_personal.styles.styles import Size

def  header(data: Data) -> rx.Component:
    return rx.flex(
        rx.image(
            src=data.avatar,
            class_name="shadow-xl rounded-xl w-40 h-40",
            alt="Logo R"
        ),
        rx.vstack(
            heading(data.name, h1=True),
            heading(data.job_position),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit",
                class_name="text-sm md:text-lg"
            ),
            media(data.media),
            spacing=Size.DEFAULT.value
        ),
        width="100%",
        spacing=Size.LARGE.value,
        flex_direction=["column", "column", "row", "row"],
        align_items="center",
        class_name="box-s"
    )