from lona.html import Div, Node

from lona_picocss.html.base import PicocssNode


class Container(PicocssNode, Div):
    CLASS_LIST = ['container']


class Mark(PicocssNode, Div):
    TAG_NAME = 'mark'


class Header(PicocssNode, Node):
    TAG_NAME = 'header'


class Footer(PicocssNode, Node):
    TAG_NAME = 'footer'


class Figure(PicocssNode, Node):
    TAG_NAME = 'figure'


class Article(PicocssNode, Node):
    TAG_NAME = 'article'


class Grid(PicocssNode, Div):
    CLASS_LIST = ['grid']
