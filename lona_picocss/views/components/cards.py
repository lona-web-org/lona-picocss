from lona import View

from lona_picocss.html import HTML, Card, Grid, Div, H1, H2


class CardsView(View):
    def handle_request(self, request):
        self.set_title('Cards')

        return HTML(
            H1('Cards'),

            Grid(
                Div(
                    H2('Simple Card'),
                    Card('Card Body'),
                ),
                Div(
                    H2('Card With Header'),
                    Card(
                        'Card Body',
                        header='Card Header',
                    ),
                ),
            ),
            Grid(
                Div(
                    H2('Card With Footer'),
                    Card(
                        'Card Body',
                        footer='Card Footer',
                    ),
                ),
                Div(
                    H2('Card With Header And Footer'),
                    Card(
                        'Card Body',
                        header='Card Header',
                        footer='Card Footer',
                    ),
                ),
            ),
        )
