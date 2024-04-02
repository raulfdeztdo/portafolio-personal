import reflex as rx

from portafolio_personal.components.heading import heading
from portafolio_personal.styles.styles import Size
from portafolio_personal.translations import get_translation

def about(description: str, lang) -> rx.Component:
    return rx.vstack(
        heading(get_translation("about_title", lang), True),
        rx.text(description),
        class_name="box-s text-justify",
        spacing=Size.LARGE.value,
    )