import reflex as rx

from portafolio_personal.components.heading import heading
from portafolio_personal.styles.styles import Size


def tech_stack() -> rx.Component:
    return rx.vstack(
        heading("Tecnologías"),
        rx.flex(
            *[
                rx.badge(
                    rx.icon("code"),
                    rx.text(f"Stack{index}"),
                    size="2"
                )
                for index in range(0, 10)

            ],
            wrap="wrap",
            spacing=Size.DEFAULT.value
        ),
        spacing=Size.DEFAULT.value
    )