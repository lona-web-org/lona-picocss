from lona.html import CLICK, Nav, Ul, Div, Li, A

from lona_picocss.html.base import PicocssNode


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
