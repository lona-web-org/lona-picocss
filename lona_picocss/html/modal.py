from lona.html import Node, CLICK, Div, A

from lona_picocss.html.generic import Footer, Article
from lona_picocss.html.base import PicocssNode


class Modal(PicocssNode, Node):
    # TODO: add support for headers
    # TODO: make animations optional

    TAG_NAME = 'dialog'
    WIDGET = 'LonaPicocssModalWidget'
    EVENTS = [CLICK]

    def __init__(self, closeable=True):
        super().__init__()

        self.widget_data = {
            'open': False,
        }

        self.nodes = [
            Article(
                A(
                    href='#',
                    _aria_label='Close',
                    _class='close',
                    events=[CLICK],
                    handle_click=lambda i: self.close(),
                ),
                Div(),
            ),
        ]

        self.closeable = closeable

    def handle_input_event(self, input_event):
        if input_event.target_node == self and self.closeable:
            self.close()

    @property
    def closeable(self):
        return self.nodes[0][0].style.get('display', '') != 'none'

    @closeable.setter
    def closeable(self, new_value):
        if new_value:
            if 'display' in self.nodes[0][0].style:
                self.nodes[0][0].style.pop('display')

        else:
            self.nodes[0][0].style['display'] = 'none'

    def open(self):
        self.widget_data['open'] = True

    def close(self):
        self.widget_data['open'] = False

    def get_body(self):
        with self.lock:
            if isinstance(self.nodes[0][-1], Footer):
                return self.nodes[0][-2]

            return self.nodes[0][-1]

    def get_footer(self):
        with self.lock:
            if not isinstance(self.nodes[0][-1], Footer):
                self.nodes[0].append(Footer())

            return self.nodes[0][-1]
