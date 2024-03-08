import reflex as rx

from portafolio_personal.components.icon_button import icon_button
from portafolio_personal.data import Media
from portafolio_personal.styles.styles import Size

def media(data: Media) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"mailto:{data.email}",
            data.email,
            True
        ),
        rx.hstack(
            icon_button(
                "file-text",
                data.cv,
                "",
                False
            ),
            icon_button(
                "linkedin",
                data.linkedin,
                "",
                False
            ),
            icon_button(
                "github",
                data.github,
                "",
                False
            ),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )