from lona import View

from lona_picocss.html import (
    InlineButton,
    Switch,
    Label,
    Modal,
    HTML,
    Grid,
    Div,
    H1,
    H3,
    P,
)


class ModalView(View):
    STOP_DAEMON_WHEN_VIEW_FINISHES = False

    def set_is_daemon(self, input_event):
        self.is_daemon = input_event.node.value

    def set_closable(self, input_event):
        self.modal.closeable = input_event.node.value

    def handle_request(self, request):
        self.set_title('Modal')

        self.modal = Modal()

        self.modal.get_body().nodes = [
            H3('Modal'),
            P("""
                Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed
                diam nonumy eirmod tempor invidunt ut labore et dolore magna
                aliquyam erat, sed diam voluptua. At vero eos et accusam et
                justo duo dolores et ea rebum. Stet clita kasd gubergren, no
                sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem
                ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
                nonumy eirmod tempor invidunt ut labore et dolore magna
                aliquyam erat, sed diam voluptua. At vero eos et accusam et
                justo duo dolores et ea rebum. Stet clita kasd gubergren, no
                sea takimata sanctus est Lorem ipsum dolor sit amet.
            """)
        ]

        self.modal.get_footer().nodes = [
            InlineButton(
                'Cancel',
                secondary=True,
                handle_click=lambda i: self.modal.close(),
            ),
            InlineButton(
                'Confirm',
                handle_click=lambda i: self.modal.close(),
            ),
        ]

        return HTML(
            H1('Modal'),
            Grid(
                Div(
                    Label(
                        'Daemon View ',
                        Switch(
                            value=self.is_daemon,
                            handle_change=self.set_is_daemon,
                        ),
                    ),
                    Label(
                        'Closable ',
                        Switch(
                            value=self.modal.closeable,
                            handle_change=self.set_closable,
                        ),
                    ),
                ),
                Div(
                    InlineButton(
                        'Open Modal',
                        handle_click=lambda i: self.modal.open(),
                    ),
                ),
            ),
            self.modal,
        )
