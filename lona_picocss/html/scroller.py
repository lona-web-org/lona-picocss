from lona.html import Div, Pre


class ScrollerBody(Div):
    CLASS_LIST = ['scroller-body']


class ScrollerAnchor(Div):
    CLASS_LIST = ['scroller-anchor']


class Scroller:
    CLASS_LIST = ['scroller']
    WIDGET = 'LonaPicocssScrollerWidget'

    def __init__(self, *args, width='', height='', lines=None, **kwargs):
        super().__init__(**kwargs)

        self.body = ScrollerBody(*args)
        self.anchor = ScrollerAnchor()

        self.nodes = [
            self.body,
            self.anchor,
        ]

        self.width = width
        self.height = height
        self.lines = lines

    # width
    @property
    def width(self):
        return self.style.get('width', '')

    @width.setter
    def width(self, new_value):
        self.style['width'] = new_value

    # height
    @property
    def height(self):
        return self.style.get('height', '')

    @height.setter
    def height(self, new_value):
        self.style['height'] = new_value

    # methods
    def _trim(self):
        # we don't slice here, so no node has to be resent

        if self.lines is None:
            return

        while len(self.body.nodes) > self.lines:
            self.body.nodes.pop(0)

    def append(self, node):
        with self.lock:
            self.body.append(node)
            self._trim()

    def insert(self, index, node):
        with self.lock:
            self.body.insert(index, node)
            self._trim()

    def extend(self, node_list):
        with self.lock:
            self.body.extend(node_list)
            self._trim()

    def clear(self):
        self.body.clear()


class ScrollerDiv(Scroller, Div):
    pass


class ScrollerPre(Scroller, Pre):
    pass
