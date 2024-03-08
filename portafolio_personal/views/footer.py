import datetime
import reflex as rx

from portafolio_personal.components.media import media
from portafolio_personal.data import Data
from portafolio_personal.styles.styles import Size

def footer(data: Data, lang) -> rx.Component:
    return rx.vstack(
        rx.text(f"{data.name} © {datetime.datetime.now().year}"),
        media(data.media),
        spacing=Size.DEFAULT.value
    )