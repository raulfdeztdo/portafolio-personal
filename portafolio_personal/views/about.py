import reflex as rx

from portafolio_personal.components.heading import heading

def about() -> rx.Component:
    return rx.vstack(
        heading("Sobre mí"),
        rx.text("Descripción de mi vida y mi carrera profesional.")
    )