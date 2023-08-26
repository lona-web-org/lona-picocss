from lona import View

from lona_picocss import settings

from lona_picocss.html import (
    Select2 as Select,
    Option2 as Option,
    InlineButton,
    TextInput,
    TextArea,
    Progress,
    Button,
    CHANGE,
    Switch,
    Strong,
    Label,
    Modal,
    HTML,
    Card,
    Grid,
    Tabs,
    Div,
    Pre,
    H1,
    H3,
    Br,
    P,
)


class SettingsView(View):
    SPACER = [4, 10, 14, 17, 29]

    def refresh(self):
        return {
            'http_redirect': self.server.reverse('picocss__settings'),
        }

    def handle_change(self, input_event):
        name = input_event.node.state['name']
        value = input_event.node.value

        settings.set(name, value)
        settings.render_theme()

        return self.refresh()

    def apply(self, input_event):
        settings.render_theme()

        return self.refresh()

    def reset(self, input_event):
        settings.reset()
        settings.load_lona_settings()
        settings.render_theme()

        return self.refresh()

    def reset_to_defaults(self, input_event):
        settings.reset()
        settings.render_theme()

        return self.refresh()

    def handle_request(self, request):
        self.set_title('Pico.css Settings')

        html = HTML(
            H1('Pico.css Settings'),

            P(
                'Configure Pico.css to your liking and copy all settings from ',
                Strong('Compiled Settings'),
                ' to your settings.',
                Br(),
                'To unset a value, just leave it empty.',
            ),

            Grid(
                Div(),
                Div(
                    Grid(
                        Button(
                            'Reset',
                            secondary=True,
                            handle_click=self.reset,
                        ),
                        Button(
                            'Reset to defaults',
                            secondary=True,
                            handle_click=self.reset_to_defaults,
                        ),
                        Button(
                            'Apply',
                            handle_click=self.apply,
                        ),
                    ),
                    Label(
                        'Compiled Settings',
                        Pre(
                            style={
                                'min-height': '20em',
                            },
                        ),
                    ),
                    Label('Preview'),
                    Div(id='preview'),
                ),
            ),
        )

        # settings prefix
        settings_prefix = ''

        project_type = self.server.settings.get(
            'PICOCSS_LONA_PROJECT_TYPE',
            'project',
        )

        if project_type == 'app':
            settings_prefix = 'app.settings.'

        # setup settings
        settings_pre = html.query_selector('pre')
        settings_form = html[2][0]

        index = -1

        for name in settings.get_names():
            slug = name[len('PICOCSS_'):].replace('_', '-').lower()
            verbose_name = name[len('PICOCSS_'):].replace('_', ' ').title()
            value = settings.get(name)
            values = settings.get_default(name, value)

            # unsupported settings
            if name in ('PICOCSS_DEBUG', 'PICOCSS_NAVIGATION', ):
                continue

            index += 1

            # show exceptions
            if name == 'PICOCSS_SHOW_EXCEPTIONS':
                if callable(value):
                    value = True

            # string values
            if isinstance(values, str):
                field = Label(
                    verbose_name,
                    TextInput(
                        value=value,
                        placeholder='not set',
                        bubble_up=True,
                        handle_change=self.handle_change,
                        state={'name': name},
                        id=f'setting_{slug}',
                    ),
                )

                field[1].events = [CHANGE]

            # selects
            elif isinstance(values, list):
                field = Label(
                    verbose_name,
                    Select(
                        *(Option(i.title(), value=i, selected=i == value)
                          for i in values),
                        bubble_up=True,
                        handle_change=self.handle_change,
                        state={'name': name},
                        id=f'setting_{slug}',
                    ),
                )

            # switches
            elif isinstance(values, bool):
                field = Label(
                    verbose_name + ' ',
                    Switch(
                        value=value,
                        bubble_up=True,
                        handle_change=self.handle_change,
                        state={'name': name},
                        id=f'setting_{slug}',
                    ),
                )

            # catch all unsupported values
            else:
                continue

            # add field to form
            settings_form.append(field)

            if index in self.SPACER:
                settings_form.append(Br())
                settings_form.append(Br())

            # add config variable to compiled output
            default = settings.get_default(name)

            if isinstance(default, list) and len(default) > 0:
                default = default[0]

            if value != default:
                settings_pre.write_line(
                    f'{settings_prefix}{name} = {repr(value)}',
                )

        # empty settings
        if len(settings_pre.nodes) == 0:
            settings_pre.set_text('# nothing to configure\n\n')

        # setup preview
        preview = html.query_selector('#preview')

        # tabs
        tabs = Tabs()

        tabs.get_tab('Tab 1').nodes = ['Tab Content 1']
        tabs.get_tab('Tab 2').nodes = ['Tab Content 2']

        # modal
        modal = Modal()

        modal.get_body().nodes = [
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

        modal.get_footer().nodes = [
            InlineButton(
                'Cancel',
                secondary=True,
                handle_click=lambda i: modal.close(),
            ),
            InlineButton(
                'Confirm',
                handle_click=lambda i: modal.close(),
            ),
        ]

        preview.nodes = [
            Grid(
                Button('Button'),
                Button('Secondary Button', secondary=True),
                Button('Outlined Button', outline=True),
            ),
            Select(
                Option('Select', value='select'),
                Option('Option 1', value='option-1'),
                Option('Option 2', value='option-2'),
                Option('Option 3', value='option-3'),
            ),
            TextInput(value='Text Input'),
            TextInput(type='date'),
            TextArea(placeholder='Text Area'),
            Progress(value=35),
            Card('Card'),
            Button('Modal', handle_click=lambda i: modal.open()),
            modal,
            tabs,
        ]

        return html
