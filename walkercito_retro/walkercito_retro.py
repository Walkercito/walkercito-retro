import reflex as rx

import walkercito_retro.styles.styles as styles

from walkercito_retro import data
from walkercito_retro.styles.styles import Size, EmSize, MAX_WIDTH
from walkercito_retro.views.header import header

DATA = data.data


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(DATA),
            spacing = Size.MEDIUM.value,
            padding_x = EmSize.MEDIUM.value,
            padding_y = EmSize.BIG.value,
            max_width = MAX_WIDTH,
            width = "100%"
        )
    )


app = rx.App(
    stylesheets = styles.STYLESHEETS,
    style = styles.BASE_STYLE
)
app.add_page(
    index,
    title = DATA.title,
    description = DATA.description,
    image = DATA.image,
    meta=[
        {"name": "og:title", "content": DATA.title},
        {"name": "og:description", "content": DATA.description},
        {"name": "og:image", "content": DATA.image}
    ]
)