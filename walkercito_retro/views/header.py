import reflex as rx

from walkercito_retro.data import Data
from walkercito_retro.styles.styles import Size
from walkercito_retro.components.heading import heading



def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src = data.avatar,
            size = Size.MEDIUM.value 
        ),
        rx.vstack(
            heading(data.name, True),
            heading(data.skill),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display = "inherit"
            ),
        )
    )