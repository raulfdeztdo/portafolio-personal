import reflex as rx

from portafolio_personal.components.icon_badge import icon_badge
from portafolio_personal.components.icon_button import icon_button
from portafolio_personal.data import Info
from portafolio_personal.styles.styles import IMAGE_HEIGHT, Size, EmSize

def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text(info.subtitle),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    class_name="text-slate-200"
                ),
                rx.cond(
                    info.skills,
                    rx.flex(
                        *[
                            rx.badge(
                                rx.box(
                                    class_name=skill.icon
                                ),
                                skill.name,
                                color_scheme="gray"
                            )
                            for skill in info.skills

                        ],
                        wrap="wrap",
                        spacing=Size.DEFAULT.value
                    )
                ),
                rx.hstack(
                    rx.cond(
                        info.url != "",
                        icon_button(
                            "link",
                            info.url,
                        )
                    ),
                    rx.cond(
                        info.github != "",
                        icon_button(
                            "github",
                            info.github,
                        )
                    )
                ),
                spacing=Size.DEFAULT.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        rx.cond(
            info.image != "",
            rx.image(
                src=info.image,
                height=IMAGE_HEIGHT,
                aspect_ratio="1",
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover"
            )
        ),
        rx.vstack(
            rx.cond(
                info.dates != "",
                rx.flex(
                    *[
                        rx.badge(date)
                        for date in info.dates
                    ],
                    wrap="wrap",
                    spacing=Size.DEFAULT.value,
                    justify_content="right",
                    flex_direction="column"
                )
            ),
            rx.cond(
                info.certificate != "",
                icon_button(
                    "shield-check",
                    info.certificate,
                    solid=True
                )
            ),
            spacing=Size.SMALL.value,
            align="end"
        ),
        flex_direction=["column-reverse ", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )