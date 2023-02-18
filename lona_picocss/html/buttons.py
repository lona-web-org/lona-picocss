from lona.html import Node, CLICK

from lona_picocss.html.base import PicocssNode


class _Button(PicocssNode, Node):
    # TODO: add support for .contrast

    EVENTS = [CLICK]

    def __init__(self, *args, secondary=False, outline=False, **kwargs):
        super().__init__(*args, **kwargs)

        self.secondary = secondary
        self.outline = outline

    # secondary
    @property
    def secondary(self):
        return 'secondary' in self.class_list

    @secondary.setter
    def secondary(self, new_value):
        if new_value:
            self.class_list.add('secondary')

        else:
            self.class_list.remove('secondary')

    # outline
    @property
    def outline(self):
        return 'outline' in self.class_list

    @outline.setter
    def outline(self, new_value):
        if new_value:
            self.class_list.add('outline')

        else:
            self.class_list.remove('outline')


class Button(_Button):
    TAG_NAME = 'button'


class InlineButton(_Button):
    TAG_NAME = 'a'

    ATTRIBUTES = {
        'role': 'button',
        'href': '#',
    }