from typing import List
import reflex as rx

from portafolio_personal.components.card_detail import card_detail
from portafolio_personal.components.heading import heading
from portafolio_personal.styles.styles import Size
from portafolio_personal.data import Extra

def extra(extras: List[Extra], lang) -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        rx.mobile_only(
            rx.vstack(
                *[
                    card_detail(extra)
                    for extra in extras
                ],
                spacing=Size.DEFAULT.value
            ),
            width="100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *[
                    card_detail(extra)
                    for extra in extras
                ],
                spacing=Size.DEFAULT.value,
                columns="3",
            ),
            width="100%",
        ),
        spacing=Size.DEFAULT.value,
        width="100%",
        class_name="box-s"
    )