from lona.html import Node

from lona_picocss.html.generic import Header, Footer
from lona_picocss.html.base import PicocssNode


class Card(PicocssNode, Node):
    TAG_NAME = 'article'

    def __init__(self, *args, nodes=None, header=None, footer=None, **kwargs):
        super().__init__(*args, **kwargs)

        if nodes:
            self.nodes = nodes

        if header:
            self.get_header().nodes = header

        if footer:
            self.get_footer().nodes = footer

    def get_header(self):
        with self.lock:
            if(len(self.nodes) == 0 or
               not isinstance(self.nodes[0], Header)):

                self.insert(0, Header())

            return self.nodes[0]

    def get_footer(self):
        with self.lock:
            if(len(self.nodes) == 0 or
               not isinstance(self.nodes[-1], Footer)):

                self.append(Footer())

            return self.nodes[-1]
