import reflex as rx
import portafolio_personal.data as data_es, portafolio_personal.data as data_en
from portafolio_personal.components.navbar import navbar
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
                src="/darkmode.js",
            ),
            navbar(lang),
            rx.center(
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
                    width="100%"
                ),
                class_name="flex mt-14 justify-center items-center w-full text-slate-900 dark:text-slate-200 bg-slate-200 dark:bg-slate-900"
            ),
            class_name="relative"
        )

class HeadTags(rx.Component):
    def render(self):
        return rx.html("""
            <link rel="apple-touch-icon" sizes="180x180" href="/assets/images/favicon/apple-touch-icon.png">
            <link rel="icon" type="image/png" sizes="32x32" href="/assets/images/favicon/favicon-32x32.png">
            <link rel="icon" type="image/png" sizes="16x16" href="/assets/images/favicon/favicon-16x16.png">
            <link rel="manifest" href="/assets/images/favicon/site.webmanifest">
            <link rel="mask-icon" href="/assets/images/favicon/safari-pinned-tab.svg" color="#5bbad5">
            <meta name="msapplication-TileColor" content="#da532c">
            <meta name="theme-color" content="#ffffff">
        """)

app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    head_tags=HeadTags(),
)

app.add_page(index("es"), route="/", title=get_translation("page_title", "es"))
app.add_page(index("en"), route="/en", title=get_translation("page_title", "en"))