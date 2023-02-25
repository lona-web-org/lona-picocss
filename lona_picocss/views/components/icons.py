from lona import View

from lona_picocss.html import (
    TextInput,
    Label,
    HTML,
    Grid,
    Card,
    Icon,
    Div,
    H1,
)


class IconsView(View):
    ICONS_PER_ROW = 6

    def update_icons(self, input_event):
        with self.html.lock:
            self.icons.clear()

            # filter icons
            icon_names = Icon.ICON_NAMES.copy()

            if self.search_string.value:
                for name in Icon.ICON_NAMES:
                    if self.search_string.value not in name:
                        icon_names.remove(name)

            # add icons to view
            if not icon_names:
                self.icons.set_text('No Matches')

                return

            for index, name in enumerate(icon_names):
                if index == 0 or index % self.ICONS_PER_ROW == 0:
                    self.icons.append(Grid())

                self.icons[-1].append(
                    Card(
                        Icon(
                            name,
                            stroke_width=self.stroke_width.value,
                            color=self.color.value,
                            width=self.width.value,
                            height=self.height.value,
                        ),
                        footer=Div(
                            name,
                            style={
                                'font-size': '70%',
                            },
                        ),
                        style={
                            'text-align': 'center',
                        },
                    ),
                )

            # filler
            if len(icon_names) % self.ICONS_PER_ROW == 0:
                return

            empty_spaces = (self.ICONS_PER_ROW -
                            (len(icon_names) % self.ICONS_PER_ROW))

            for _ in range(empty_spaces):
                self.icons[-1].append(Div())

    def handle_request(self, request):
        self.set_title('Icons')

        self.icons = Div()

        # form
        icon = Icon(name=Icon.ICON_NAMES[0])

        self.search_string = TextInput(
            placeholder='Name',
            handle_change=self.update_icons,
        )

        self.stroke_width = TextInput(
            value=icon.stroke_width,
            handle_change=self.update_icons,
        )

        self.color = TextInput(
            value=icon.color,
            placeholder='Color',
            handle_change=self.update_icons,
        )

        self.width = TextInput(
            value=icon.width,
            placeholder='Width',
            handle_change=self.update_icons,
        )

        self.height = TextInput(
            value=icon.height,
            placeholder='Height',
            handle_change=self.update_icons,
        )

        self.html = HTML(
            H1('Icons'),

            # form
            Div(
                Grid(
                    Div(
                        Label(
                            'Search',
                            self.search_string,
                        ),
                    ),
                    Div(),
                ),
                Grid(
                    Div(
                        Label(
                            'Stroke Width',
                            self.stroke_width,
                        ),
                    ),
                    Div(
                        Label(
                            'Color',
                            self.color,
                        ),
                    ),
                ),
                Grid(
                    Div(
                        Label(
                            'Width',
                            self.width,
                        ),
                    ),
                    Div(
                        Label(
                            'Height',
                            self.height,
                        ),
                    ),
                ),
                _id='form',
            ),

            # icon
            self.icons,
        )

        self.update_icons(None)

        # this gets used for screenshots
        if 'no-form' in request.GET:
            self.html.query_selector('#form').hide()

        return self.html
