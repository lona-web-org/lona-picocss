from lona.html import (
    TextInput as BaseTextInput,
    TextArea as BaseTextArea,
    CheckBox,
)

from lona_picocss.html.base import PicocssNode


class TextInput(PicocssNode, BaseTextInput):
    # TODO: add support for valid and invalid

    pass


class TextArea(PicocssNode, BaseTextArea):
    # TODO: add support for valid and invalid

    pass


class Switch(PicocssNode, CheckBox):
    ATTRIBUTES = {
        'type': 'checkbox',
        'role': 'switch',
    }
