from enum import Enum
import reflex as rx

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"

class Size(Enum):
    ZERO = "0" # 0px
    SMALL = "2" # 8px / 0.5em
    DEFAULT = "4" # 16px / 1em
    MEDIUM = "6" # 32px / 2em
    LARGE = "8" # 48px

class EmSize(Enum):
    DEFAULT = "1em" # 16px
    MEDIUM = "2em" # 32px
    LARGE = "4em" # 64px

STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer",
    }
}