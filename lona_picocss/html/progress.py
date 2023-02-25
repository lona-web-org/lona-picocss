from lona.html import Node

from lona_picocss.html.base import PicocssNode


class Progress(PicocssNode, Node):
    TAG_NAME = 'progress'

    ATTRIBUTES = {
        'max': '100',
    }

    def __init__(self, value=None):
        super().__init__()

        self.value = value

    @property
    def value(self):
        with self.lock:
            if 'value' not in self.attributes:
                return None

            return int(self.attributes['value'])

    @value.setter
    def value(self, new_value):
        if new_value is None:
            if 'value' in self.attributes:
                self.attributes.pop('value')

        else:
            self.attributes['value'] = int(new_value)
