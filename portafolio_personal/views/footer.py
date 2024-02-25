import reflex as rx

from portafolio_personal.components.media import media
from portafolio_personal.styles.styles import Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.text("Raúl Fernández Tirado © 2024"),
        media(),
        spacing=Size.DEFAULT.value
    )