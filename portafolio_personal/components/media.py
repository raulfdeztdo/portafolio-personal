import reflex as rx

from portafolio_personal.components.icon_button import icon_button
from portafolio_personal.styles.styles import Size

def media() -> rx.Component:
    return rx.hstack(
        icon_button(
            "mail",
            "mailto:raulfdeztdo@gmail.com",
            "raulfdeztdo@gmail.com",
            True
        ),
        icon_button(
            "file-text",
            "https://drive.google.com/file/d/1KkItvmS77QDzzr7haImq5akRdoIxrxX0/view",
            "",
            False
        ),
        icon_button(
            "linkedin",
            "https://www.linkedin.com/in/raulfdeztdo/",
            "",
            False
        ),
        icon_button(
            "github",
            "https://github.com/raulfdeztdo",
            "",
            False
        ),
    )