from datetime import datetime

from lona import View

from lona_picocss.html import HTML, H1, H2, Div, ScrollerDiv, ScrollerPre, Card


class ScrollerView(View):
    def append_timestamp(self):
        self.scroller_div.append(Div(f'{str(datetime.now())}'))
        self.scroller_pre.append(f'{str(datetime.now())}\n')

    def handle_request(self, request):
        self.set_title('Scroller')

        self.scroller_div = ScrollerDiv(
            'Begin',
            height='250px',
        )

        self.scroller_pre = ScrollerPre(
            'Begin\n',
            height='250px',
        )

        self.html = HTML(
            H1('Scroller'),
            H2('Div'),
            self.scroller_div,

            H2('Pre'),
            self.scroller_pre,
        )

        for _ in range(5):
            self.append_timestamp()

        while True:
            self.show(self.html)
            self.append_timestamp()
            self.sleep(1)
