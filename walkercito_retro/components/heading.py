import reflex as rx

from walkercito_retro.styles.styles import Size


def heading(text: str, h1 = False) -> rx.Component:
    return rx.heading(
        text,
        as_ = "h1" if h1 else "h2",
        size = Size.MEDIUM.value if h1 else Size.SMALL.value
    )