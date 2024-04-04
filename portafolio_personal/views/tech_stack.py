from typing import List
import reflex as rx

from portafolio_personal.components.heading import heading
from portafolio_personal.data import Skill
from portafolio_personal.styles.styles import Size
from portafolio_personal.translations import get_translation


def tech_stack(skills: List[Skill] ,lang) -> rx.Component:
    return rx.vstack(
        heading(get_translation("skills_title", lang), True),
        rx.box(
            *[
                rx.badge(
                    rx.box(
                        class_name=skill.icon,
                        font_size="24px"
                    ),
                    rx.text(skill.name, class_name="justify-center"),
                    size="2",
                    class_name="justify-center"
                )
                for skill in skills

            ],
            class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4 mx-auto",
        ),
        width="100%",
        spacing=Size.LARGE.value,
        class_name="box-s"
    )