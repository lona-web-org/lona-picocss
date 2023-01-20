from lona.html import HTML, Button, Div, H1
from lona import LonaApp, LonaView

from lona_picocss import install_picocss

app = LonaApp(__file__)

install_picocss(app, debug=True)

app.run()