from enum import Enum
import reflex as rx

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"
IMG_LOGO = "/images/logo.png"
IMG_LOGO_TRANSPARENT = "/images/R-Logo-Transparent.png"
IMG_LOGO_TR_LIGHT_SHADOW = "/images/R-Logo-Light-Shadow.png"
IMG_LOGO_TR_DARK_SHADOW = "/images/R-Logo-Dark-Shadow.png"
IMG_LOGO_NAVBAR = "/images/logo-navbar.png"

class Size(Enum):
    ZERO = "0" # 0px
    SMALL = "2" # 8px / 0.5em
    DEFAULT = "4" # 16px / 1em
    MEDIUM = "6" # 32px / 2em
    LARGE = "8" # 48px
    EXTRALARGE = "9" # 64px

class EmSize(Enum):
    DEFAULT = "1em" # 16px
    MEDIUM = "2em" # 32px
    LARGE = "4em" # 64px

STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
    "/fonts/fonts.css",
    "/switch-dark-light-mode.css",
    "/styles.css",
]

BASE_STYLE = {
    "fontFamily": "'Rubik', sans-serif",
    "backgroundColor": "#334155 !important",
    rx.button: {
        "--cursor-button": "pointer",
    }
}