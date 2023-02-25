from lona.html import Node

from lona_picocss.html.base import PicocssNode


class A(PicocssNode, Node):
    TAG_NAME = 'a'

    def __init__(self, *args, secondary=False, contrast=False, **kwargs):
        super().__init__(*args, **kwargs)

        self.secondary = secondary
        self.contrast = contrast

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
