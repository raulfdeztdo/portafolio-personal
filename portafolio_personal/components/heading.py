import reflex as rx

from portafolio_personal.styles.styles import Size

def heading(text: str, h1=False) -> rx.Component:
    return rx.flex(
        rx.tablet_and_desktop(
            rx.heading(
                text,
                as_="h2",
                size=Size.LARGE.value if h1 else Size.MEDIUM.value,
                font_family="Rubik",
            )
        ),
        rx.mobile_only(
            rx.heading(
                text,
                as_="h2",
                size=Size.MEDIUM.value if h1 else Size.SMALL.value,
                font_family="Rubik",
            )
        )
    )