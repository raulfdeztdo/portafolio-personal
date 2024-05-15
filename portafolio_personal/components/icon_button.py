import reflex as rx

def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "surface",
            title="Button: " + icon + " - " + text
        ),
        href=url,
        is_external=True,
        class_name="flex justify-center",
        title="Link: " + icon + " - " + text
    )
