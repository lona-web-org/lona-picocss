from lona import View

from lona_picocss.html import HTML, Progress, H1, H2


class ProgressView(View):
    def handle_request(self, request):
        self.set_title('Progress')

        return HTML(
            H1('Progress'),

            H2('Normal Progress'),
            Progress(value=75),

            H2('Indeterminate Progress'),
            Progress(value=None),
        )
