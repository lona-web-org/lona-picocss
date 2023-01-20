from lona.html import *  # NOQA
from lona.static_files import StyleSheet, Script, SORT_ORDER

from lona.html import (
    TextInput as BaseTextInput,
    TextArea as BaseTextArea,
    CheckBox,
    CLICK,
    Node,
    Div,
    Nav,
    Ul,
    Li,
)


class PicocssNode:
    STATIC_FILES = [
        StyleSheet(
            name='pico.min.css',
            path='static/lona-picocss/dist/pico.min.css',
            url='/lona-picocss/pico.min.css',
            sort_order=SORT_ORDER.FRAMEWORK,
        ),
        Script(
            name='picocss-widgets.js',
            path='static/lona-picocss/picocss-widgets.js',
            url='/lona-picocss/picocss-widgets.js',
            sort_order=SORT_ORDER.LIBRARY,
        ),
    ]


# generic nodes ###############################################################
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


# links #######################################################################
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


# inputs ######################################################################
class TextInput(PicocssNode, BaseTextInput):
    # TODO: add support for valid and invalid

    pass


class TextArea(PicocssNode, BaseTextArea):
    # TODO: add support for valid and invalid

    pass


# cards #######################################################################
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


# modal #######################################################################
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


# button ######################################################################
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


# switch ######################################################################
class Switch(PicocssNode, CheckBox):
    ATTRIBUTES = {
        'type': 'checkbox',
        'role': 'switch',
    }


# tabs ########################################################################
class Tabs(PicocssNode, Div):
    def __init__(self, *tabs):
        super().__init__()

        self.nodes = [
            Nav(Ul()),
            Div(),
        ]

        self.ul = self.nodes[0][0]
        self.tabs = self.nodes[1]

        self._tabs = {}
        self._active_tab_index = 0

        if tabs:
            for index in range(0, len(tabs), 2):
                tab_name = tabs[index]
                tab = self.get_tab(tab_name)
                tab.nodes = tabs[index+1]

            self._render()

    def _handle_label_click(self, input_event):
        with self.lock:
            li = input_event.node.closest('li')
            self._active_tab_index = self.ul.nodes.index(li)

            self._render()

    def _render(self):
        for index, li in enumerate(self.ul):
            tab = self.tabs[index]

            # active tab
            if index == self._active_tab_index:
                li[0].class_list.remove('secondary')
                tab.show()

            # inactive tabs
            else:
                li[0].class_list.add('secondary')
                tab.hide()

    def get_tab(self, name):
        with self.lock:

            # create tab
            if name not in self._tabs:
                tab_label = Li(
                    A(
                        name,
                        href='#',
                        events=[CLICK],
                        handle_click=self._handle_label_click,
                    ),
                )

                tab = Div()

                self.ul.append(tab_label)
                self.tabs.append(tab)

                self._tabs[name] = tab

                self._render()

            # get tab
            tab = self._tabs[name]

        return tab


# progress ####################################################################
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
