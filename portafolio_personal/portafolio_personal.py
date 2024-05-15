import reflex as rx
import portafolio_personal.data as data_es, portafolio_personal.data as data_en
from portafolio_personal.components.navbar import navbar
from portafolio_personal.components.banner import banner
from portafolio_personal.views.about import about
from portafolio_personal.views.extra import extra
from portafolio_personal.views.footer import footer
from portafolio_personal.views.header import header
from portafolio_personal.styles.styles import MAX_WIDTH, EmSize, Size, BASE_STYLE, STYLESHEETS
from portafolio_personal.views.info import info
from portafolio_personal.views.tech_stack import tech_stack
from portafolio_personal.translations import get_translation

def index(lang='es') -> rx.Component:
    DATA = data_es.data_es if lang == 'es' else data_en.data_en
    return rx.vstack(
        rx.script(
            src="/scripts.js",
        ),
        navbar(),
        banner(lang),
        rx.center(
            # rx.theme_panel(),
            rx.vstack(
                header(DATA),
                about(DATA.about, lang),
                tech_stack(DATA.skills, lang),
                info(get_translation("experience_title", lang), DATA.experience, lang),
                info(get_translation("projects_title", lang), DATA.project, lang),
                info(get_translation("training_title", lang), DATA.training, lang),
                # extra(DATA.extras, lang),
                spacing=Size.LARGE.value,
                padding_x=EmSize.MEDIUM.value,
                padding_y=EmSize.LARGE.value,
                max_width=MAX_WIDTH,
                width="100%"
            ),
            class_name="flex justify-center items-center w-full text-slate-900 dark:text-slate-200 bg-slate-200 dark:bg-slate-900"
        ),
        footer(DATA, lang),
        class_name="relative",
        spacing=Size.ZERO.value
    )

app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme= rx.theme(
        accent_color="indigo"
    )
)

app.add_page(index("es"), route="/", title=get_translation("page_title", "es"))
app.add_page(index("en"), route="/en", title=get_translation("page_title", "en"))