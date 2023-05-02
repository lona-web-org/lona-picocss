from lona.html import Node, CLICK

from lona_picocss.html.base import PicocssNode


class _Button(PicocssNode, Node):
    EVENTS = [CLICK]

    def __init__(
            self,
            *args,
            secondary=False,
            outline=False,
            contrast=False,
            disabled=False,
            **kwargs,
    ):

        super().__init__(*args, **kwargs)

        self.secondary = secondary
        self.outline = outline
        self.contrast = contrast
        self.disabled = disabled

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

    # contrast
    @property
    def contrast(self):
        return 'contrast' in self.class_list

    @contrast.setter
    def contrast(self, new_value):
        if new_value:
            self.class_list.add('contrast')

        else:
            self.class_list.remove('contrast')

    # disabled
    @property
    def disabled(self):
        return 'disabled' in self.attributes

    @disabled.setter
    def disabled(self, new_value):
        if new_value:
            self.attributes['disabled'] = ''

        else:
            del self.attributes['disabled']


class Button(_Button):
    TAG_NAME = 'button'


class InlineButton(_Button):
    TAG_NAME = 'a'

    ATTRIBUTES = {
        'role': 'button',
        'href': '#',
    }