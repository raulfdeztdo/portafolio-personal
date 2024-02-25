import reflex as rx
from portafolio_personal.views.about import about
from portafolio_personal.views.extra import extra
from portafolio_personal.views.footer import footer
from portafolio_personal.views.header import header
from portafolio_personal.styles.styles import MAX_WIDTH, EmSize, Size
from portafolio_personal.views.info import info
from portafolio_personal.views.tech_stack import tech_stack

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(),
            about(),
            rx.divider(),
            tech_stack(),
            info("Experiencia"),
            info("Proyectos"),
            info("Formación"),
            extra(),
            rx.divider(),
            footer(),
            spacing=Size.LARGE.value,
            padding_y=EmSize.LARGE.value,
            max_width=MAX_WIDTH,
            width="100%",
        )
    )

app = rx.App()
app.add_page(index)
