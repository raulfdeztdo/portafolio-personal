import reflex as rx

from portafolio_personal.components.heading import heading
from portafolio_personal.styles.styles import Size
from portafolio_personal.views.info_detail import info_detail

def info(title: str) -> rx.Component:
    return rx.vstack(
        heading(title),
        info_detail(),
        spacing=Size.DEFAULT.value,
        width="100%",
    )