from lona.html import Node

from lona_picocss.html.base import FeatherNode, get_feather_icon_names


class Icon(FeatherNode, Node):
    TAG_NAME = 'i'
    WIDGET = 'LonaPicocssFeatherIconWidget'
    ICON_NAMES = get_feather_icon_names()

    def __init__(
            self,
            name,
            stroke_width=None,
            width=None,
            height=None,
            color=None,
    ):

        super().__init__()

        self.widget_data = {
            'name': name,
            'stroke-width': 2,
            'width': 24,
            'height': 24,
            'viewBox': '0 0 24 24',
            'color': '',
        }

        self._check_name()

        if stroke_width:
            self.stroke_width = stroke_width

        if width:
            self.width = width

        if height:
            self.height = height

        if color:
            self.color = color

    def _check_name(self):
        name = self.widget_data['name']

        if name not in self.ICON_NAMES:
            raise RuntimeError(
                f'Unknown icon: {self.name}. Supported icon names: {", ".join(self.ICON_NAMES)}',
            )

    def _set_view_box(self, min_x=None, min_y=None, width=None, height=None):
        with self.lock:
            view_box = self.widget_data['viewBox'].split(' ')

            view_box[0] = min_x or view_box[0]
            view_box[1] = min_y or view_box[1]
            view_box[2] = width or view_box[2]
            view_box[3] = height or view_box[3]

            self.widget_data['viewBox'] = f'{view_box[0]} {view_box[1]} {view_box[2]} {view_box[3]}'

    # properties ##############################################################
    # name
    @property
    def name(self):
        return self.widget_data['name']

    @name.setter
    def name(self, new_value):
        with self.lock:
            self.widget_data['name'] = new_value
            self._check_name()

    # stroke_width
    @property
    def stroke_width(self):
        return self.widget_data['stroke-width']

    @stroke_width.setter
    def stroke_width(self, new_value):
        self.widget_data['stroke-width'] = new_value

    # width
    @property
    def width(self):
        return self.widget_data['width']

    @width.setter
    def width(self, new_value):
        with self.lock:
            self.widget_data['width'] = new_value
            self._set_view_box(width=new_value)

    # height
    @property
    def height(self):
        return self.widget_data['height']

    @height.setter
    def height(self, new_value):
        with self.lock:
            self.widget_data['height'] = new_value
            self._set_view_box(height=new_value)

    # color
    @property
    def color(self):
        return self.widget_data['color']

    @color.setter
    def color(self, new_value):
        self.widget_data['color'] = new_value
