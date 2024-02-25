import reflex as rx

from portafolio_personal.components.icon_badge import icon_badge
from portafolio_personal.components.icon_button import icon_button
from portafolio_personal.styles.styles import IMAGE_HEIGHT, Size, EmSize

def info_detail() -> rx.Component:
    return rx.hstack(
        icon_badge("box-select"),
        rx.vstack(
            rx.text.strong("Titulo"),
            rx.text("Subtitulo"),
            rx.text(
                "Descripción",
                size=Size.SMALL.value,
                color_scheme="gray"
            ),
            rx.flex(
                *[
                    rx.badge(
                        f"Badge{index}",
                        color_scheme="gray"
                    )
                    for index in range(0, 5)

                ],
                wrap="wrap",
                spacing=Size.DEFAULT.value
            ),
            rx.hstack(
                icon_button(
                    "link",
                    ""
                ),
                icon_button(
                    "github",
                    ""
                )
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
        rx.hstack(
            rx.image(
                src="/favicon.ico",
                height=IMAGE_HEIGHT,
                aspect_ratio="1",
                border_radius=EmSize.DEFAULT.value
            ),
            rx.vstack(
                rx.badge("Años"),
                icon_button(
                    "shield-check",
                    "",
                    solid=True
                ),
                spacing=Size.DEFAULT.value,
                align="end"
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
        spacing=Size.DEFAULT.value,
        width="100%",
    )