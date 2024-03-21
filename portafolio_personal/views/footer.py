import datetime
import reflex as rx

from portafolio_personal.components.media import media
from portafolio_personal.data import Data
from portafolio_personal.styles.styles import Size
from portafolio_personal.translations import get_translation

def footer(data: Data, lang) -> rx.Component:
    return rx.vstack(
        rx.vstack(
            class_name="flex w-full h-96 bg-slate-200 dark:bg-slate-900 bg-foot-3 bg-cover",
        ),
        rx.vstack(
            rx.text(f"© {datetime.datetime.now().year} - {get_translation('footer_text', lang)}"),
            media(data.media),
            spacing=Size.DEFAULT.value,
            justify="end",
            align="center",
            class_name="flex w-full pb-24 2xl:pb-12 2xl:pt-10 text-slate-900 dark:text-slate-200 bg-slate-700",
        ),
        class_name="flex w-full bg-slate-200 dark:bg-slate-900",
        spacing=Size.ZERO.value,
    )