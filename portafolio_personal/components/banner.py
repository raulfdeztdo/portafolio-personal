import reflex as rx

from portafolio_personal.translations import get_translation

def banner(lang) -> rx.Component:
    return rx.vstack(
        rx.heading(
            "",
            id="typed-text",
            class_name="font-extrabold text-center text-base md:text-xl md:text-2xl text-slate-600 dark:text-slate-300 noto-sans-mono",
            _as="h1"
        ),
        rx.script(
            """
                const typedText = document.getElementById('typed-text');
                const messages = [
                    """ + f'"{get_translation("banner_msg_1", lang)}"' + """,
                    """ + f'"{get_translation("banner_msg_2", lang)}"' + """,
                    """ + f'"{get_translation("banner_msg_3", lang)}"' + """
                ];
                let messageIndex = 0;
                let charIndex = 0;
                let isTyping = true;

                function type() {
                    if (isTyping) {
                        if (charIndex < messages[messageIndex].length) {
                            typedText.textContent += messages[messageIndex].charAt(charIndex);
                            charIndex++;
                            setTimeout(type, 100);
                        } else {
                            isTyping = false;
                            setTimeout(resetText, 1500);
                        }
                    }
                }

                function resetText() {
                    typedText.textContent = '';
                    charIndex = 0;
                    messageIndex = (messageIndex + 1) % messages.length;
                    isTyping = true;
                    type();
                }

                type();
            """
        ),
        class_name="flex w-full mt-12 md:pb-12 h-24 md:h-64 2xl:h-48 text-slate-900 dark:text-slate-200 bg-slate-200 dark:bg-slate-900 bg-3b 2xl:bg-3 bg-cover",
        align="center",
        justify="end",
    )
