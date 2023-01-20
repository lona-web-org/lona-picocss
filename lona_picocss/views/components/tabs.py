from lona import View

from lona_picocss.html import HTML, Tabs, H1


class TabsView(View):
    def handle_request(self, request):
        self.set_title('Tabs')

        return HTML(
            H1('Tabs'),
            Tabs(
                'Tab 1',
                ['Tab Content 1'],
                'Tab 2',
                ['Tab Content 2'],
            ),
        )
