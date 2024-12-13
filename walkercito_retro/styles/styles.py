import reflex as rx

from enum import Enum

from .fonts import Font
from .colors import Color
from .colors import TextColor

MAX_WIDTH = "900px"


class EmSize(Enum):
    DEFAULT = "1em"  # 16px
    MEDIUM = "2em"
    BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2" 
    DEFAULT = "4" 
    MEDIUM = "6"  
    BIG = "8"  


STYLESHEETS = {
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap",
}


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value
}