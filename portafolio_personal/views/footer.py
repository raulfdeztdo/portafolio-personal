import datetime
import reflex as rx

from portafolio_personal.components.media import media
from portafolio_personal.data import Data
from portafolio_personal.styles.styles import Size
from portafolio_personal.translations import get_translation

def footer(data: Data, lang) -> rx.Component:
    return rx.vstack(
        rx.text(f"© {datetime.datetime.now().year} - {get_translation('footer_text', lang)}"),
        media(data.media),
        spacing=Size.DEFAULT.value
    )