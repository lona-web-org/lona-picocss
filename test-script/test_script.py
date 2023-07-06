from lona import App

from lona_picocss import install_picocss

app = App(__file__)

install_picocss(app, debug=True)

app.run()