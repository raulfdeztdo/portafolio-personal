from typing import List
import reflex as rx

from portafolio_personal.components.heading import heading
from portafolio_personal.data import Info
from portafolio_personal.styles.styles import Size
from portafolio_personal.views.info_detail import info_detail

def info(title: str,infos: List[Info], lang) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[
                info_detail(info)
                for info in infos
            ],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )