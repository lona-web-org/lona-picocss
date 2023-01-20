from lona import View

from lona_picocss.html import HTML, Button, InlineButton, Grid, Div, H1, H2


class ButtonsView(View):
    def handle_request(self, request):
        self.set_title('Buttons')

        return HTML(
            H1('Buttons'),

            Grid(
                Div(
                    H2('Block'),
                    Button('Primary Button'),
                    Button('Secondary Button', secondary=True),
                    Button('Outline Button', outline=True),
                ),
                Div(
                    H2('Inline'),
                    InlineButton('Primary Button'),
                    ' ',
                    InlineButton('Secondary Button', secondary=True),
                    ' ',
                    InlineButton('Outline Button', outline=True),
                ),
            ),
        )
