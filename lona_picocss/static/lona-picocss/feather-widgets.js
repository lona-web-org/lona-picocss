class LonaPicocssFeatherIconWidget {
    constructor(lona_window) {
        this.lona_window = lona_window;
    }

    renderSvg() {
        const icon = feather.icons[this.data.name];

        this.root_node.innerHTML = icon.toSvg(this.data);
    }

    setup() {
        this.renderSvg();
    }

    data_updated() {
        this.renderSvg();
    }
}


Lona.register_widget_class(
    'LonaPicocssFeatherIconWidget',
    LonaPicocssFeatherIconWidget,
);
