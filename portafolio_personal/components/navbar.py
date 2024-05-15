import reflex as rx

from portafolio_personal.styles.styles import Size

def navbar() -> rx.Component:
    return rx.hstack(
            rx.hstack(
                rx.text(
                    "<raul",
                    class_name="font-extrabold text-base md:text-xl md:text-2x text-slate-400 noto-sans-mono"
                ),
                rx.text(
                    "fdeztdo/>",
                    class_name="font-bold text-base md:text-xl md:text-2x text-slate-200 noto-sans-mono"
                ),
                spacing="0"
            ),
            rx.hstack(
                rx.hstack(
                    rx.button(
                        rx.text(
                            "esp",
                            class_name="font-bold text-base md:text-xl md:text-2x text-slate-300 noto-sans-mono"
                        ),
                        id="lang-es",
                        variant="ghost",
                    ),
                    rx.text(
                        "|",
                        class_name="font-extrabold text-base md:text-xl md:text-2x text-slate-500 noto-sans-mono"
                    ),
                    rx.button(
                        rx.text(
                            "eng",
                            class_name="font-bold text-base md:text-xl md:text-2x text-slate-300 noto-sans-mono mr-2"
                        ),
                        id="lang-en",
                        variant="ghost",
                    ),
                    spacing=Size.SMALL.value,
                ),
                rx.html(
                    '<input id="darkmode-toggle" type="checkbox"><label for="darkmode-toggle"><svg id="lightMode" class="sun" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 473.931 473.931" xml:space="preserve" fill="#000000" width="24" height="24"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <circle style="fill:#F2BE3E;" cx="236.966" cy="236.966" r="236.966"></circle> <circle style="fill:#F1EB75;" cx="236.966" cy="236.966" r="117.154"></circle> </g></svg><svg id="darkMode" class="moon" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 473.935 473.935" xml:space="preserve" fill="#000000" width="32" height="32"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <circle style="fill:#344E5D;" cx="236.967" cy="236.967" r="236.967"></circle> <path style="fill:#F1EB75;" d="M248.443,242.685c0-52.318,28.516-97.945,70.832-122.289c-15.757-6.601-33.055-10.26-51.21-10.26 c-73.204,0-132.549,59.341-132.549,132.549c0,73.201,59.341,132.549,132.549,132.549c18.155,0,35.453-3.663,51.21-10.267 C276.96,340.63,248.443,294.995,248.443,242.685z"></path> </g></svg></label><span class="fake-body"></span>',
                    class_name="flex darkThemeBtn"
                ),
                spacing=Size.DEFAULT.value,
                align="center",
                justify="between",
            ),
            class_name="fixed z-10 top-0 left-0 right-0 flex flex-wrap bg-slate-700 py-3 px-4 md:px-10 w-full",
            align="center",
            justify="between",
        )
