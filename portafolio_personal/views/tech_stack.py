from typing import List
import reflex as rx

from portafolio_personal.components.heading import heading
from portafolio_personal.data import Skill
from portafolio_personal.styles.styles import Size
from portafolio_personal.translations import get_translation


def tech_stack(skills: List[Skill] ,lang) -> rx.Component:
    return rx.vstack(
        heading(get_translation("skills_title", lang)),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=skill.icon,
                        font_size="24px"
                    ),
                    rx.text(skill.name),
                    size="2"
                )
                for skill in skills

            ],
            wrap="wrap",
            spacing=Size.DEFAULT.value
        ),
        spacing=Size.DEFAULT.value
    )