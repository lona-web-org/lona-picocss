from lona_picocss import settings


class LonaPicocssMiddleware:
    async def on_startup(self, data):
        settings.set_lona_server(data.server)
        settings.reset()
        settings.load_lona_settings()
        settings.render_theme()
