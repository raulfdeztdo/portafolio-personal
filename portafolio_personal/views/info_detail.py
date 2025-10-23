import reflex as rx

from portafolio_personal.components.icon_badge import icon_badge
from portafolio_personal.components.icon_button import icon_button
from portafolio_personal.data import Info
from portafolio_personal.styles.styles import Size, IMAGE_HEIGHT_LOGO_MOBILE, IMAGE_HEIGHT_LOGO_DESKTOP

def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.mobile_and_tablet(
            rx.vstack(
                rx.hstack(
                    rx.cond(
                        info.image != "",
                        rx.image(
                            src=info.image,
                            height=IMAGE_HEIGHT_LOGO_MOBILE,
                            aspect_ratio="1",
                            object_fit="contain",
                            class_name="shadow-xl rounded-xl",
                            alt=info.title
                        )
                    ),
                    rx.cond(
                        info.icon != "box-select",
                        icon_badge(info.icon),
                    ),
                    rx.cond(
                        info.dates,
                        rx.flex(
                            *[
                                rx.badge(date)
                                for date in info.dates
                            ],
                            wrap="wrap",
                            spacing=Size.SMALL.value,
                            justify_content="right",
                            flex_direction="column"
                        )
                    ),
                    spacing=Size.DEFAULT.value,
                    justify="between",
                    width="100%"
                ),
                rx.vstack(
                    rx.text.strong(info.title),
                    rx.text(info.subtitle),
                    spacing=Size.SMALL.value,
                    width="100%"
                ),
                rx.vstack(
                    rx.text(
                        info.description,
                        size=Size.SMALL.value,
                        class_name="dark:text-slate-200 text-slate-700 text-justify"
                    ),
                    rx.cond(
                        len(info.skills) > 0,
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
                ),
                # rx.vstack(
                #     rx.cond(
                #         info.certificate != "",
                #         icon_button(
                #             "shield-check",
                #             info.certificate,
                #             solid=True
                #         )
                #     ),
                #     spacing=Size.SMALL.value,
                #     align="end"
                # ),
                width="100%"
            ),
            spacing=Size.LARGE.value,
            width="100%"
        ),
        rx.desktop_only(
            rx.hstack(
                rx.cond(
                    info.image != "",
                    rx.image(
                        src=info.image,
                        height=IMAGE_HEIGHT_LOGO_DESKTOP,
                        aspect_ratio="1",
                        object_fit="contain",
                        class_name="shadow-xl rounded-xl",
                        alt=info.title
                    )
                ),
                rx.cond(
                    info.icon != "box-select",
                    icon_badge(info.icon),
                ),
                rx.vstack(
                    rx.flex(
                        rx.vstack(
                            rx.text.strong(info.title),
                            rx.text(info.subtitle),
                            width="100%"
                        ),
                        rx.cond(
                            info.dates,
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
                        flex_direction="row",
                        width="100%",
                        justify="between"
                    ),
                    rx.text(
                        info.description,
                        size=Size.SMALL.value,
                        class_name="dark:text-slate-200 text-slate-700"
                    ),
                    rx.cond(
                        len(info.skills) > 0,
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
            flex_direction=["column-reverse", "column-reverse", "row", "row"],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        width="100%",
    )