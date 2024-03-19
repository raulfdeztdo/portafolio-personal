import reflex as rx

from portafolio_personal.styles.styles import Size

def heading(text: str, h1=False) -> rx.Component:
    return rx.heading(
        text,
        as_="h1" if h1 else "h2",
        size=Size.LARGE.value if h1 else Size.MEDIUM.value,
        font_family="LexendDeca",
        class_name="font-bold"
    )