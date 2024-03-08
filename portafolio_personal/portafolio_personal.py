import reflex as rx
import portafolio_personal.data as data
from portafolio_personal.views.about import about
from portafolio_personal.views.extra import extra
from portafolio_personal.views.footer import footer
from portafolio_personal.views.header import header
from portafolio_personal.styles.styles import MAX_WIDTH, EmSize, Size, BASE_STYLE, STYLESHEETS
from portafolio_personal.views.info import info
from portafolio_personal.views.tech_stack import tech_stack
from portafolio_personal.translations import get_translation

DATA = data.data

def index(lang='es') -> rx.Component:
    return rx.center(
            # rx.theme_panel(),
            rx.vstack(
                header(DATA, lang),
                about(DATA.about, lang),
                rx.divider(),
                tech_stack(DATA.skills, lang),
                info(get_translation("experience_title", lang), DATA.experience, lang),
                info(get_translation("projects_title", lang), DATA.project, lang),
                info(get_translation("training_title", lang), DATA.training, lang),
                extra(DATA.extras, lang),
                rx.divider(),
                footer(DATA, lang),
                spacing=Size.LARGE.value,
                padding_x=EmSize.MEDIUM.value,
                padding_y=EmSize.LARGE.value,
                max_width=MAX_WIDTH,
                width="100%",
            )
        )

app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE, # type: ignore
    theme=rx.theme(
        appearance="dark",
        accentColor="sky",
        grayColor="sand",
        radius="large"
    )
)
app.add_page(index("es"), route="/", title=get_translation("page_title", "es"))
app.add_page(index("en"), route="/en", title=get_translation("page_title", "en"))
