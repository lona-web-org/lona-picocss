from lona import View

from lona_picocss.html import (
    Select2 as Select,
    Option2 as Option,
    TextInput,
    TextArea,
    CheckBox,
    Switch,
    Label,
    HTML,
    Grid,
    Div,
    H1,
    Br,
)


class FormsView(View):
    def handle_request(self, request):
        self.set_title('Forms')

        return HTML(
            H1('Forms'),
            Grid(
                Div(
                    Label(
                        'TextInput',
                        TextInput('TextInput'),
                    ),
                    Label(
                        'Select',
                        Select(
                            Option('Option 1'),
                            Option('Option 2'),
                            Option('Option 3'),
                        ),
                    ),
                    Label(
                        'TextArea',
                        TextArea('TextArea'),
                    ),
                    Label(
                        'Checkbox ',
                        CheckBox(),
                    ),
                    Br(),
                    Label(
                        'Switch ',
                        Switch(),
                    ),
                ),
                Div(),
            ),
        )
