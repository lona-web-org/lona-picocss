from tempfile import TemporaryDirectory
from pathlib import Path
import logging
import os

from lona_picocss import settings

logger = logging.getLogger('lona-picocss')


class LonaPicocssMiddleware:
    async def on_startup(self, data):
        settings.set_lona_server(data.server)
        settings.reset()
        settings.load_lona_settings()
        settings.render_theme()

        if settings.get('PICOCSS_DEBUG'):
            logger.warning('running in debug mode')


class DjangoCollectStaticMiddleware:
    # TODO: move to lona-django

    STATIC_URL_PREFIX = 'django'

    def count_static_files(self):
        count = 0

        for path in Path(self.static_root).rglob('*'):
            if path.is_dir():
                continue

            count += 1

        return count

    async def on_startup(self, data):
        from django.conf import settings as django_settings
        from django.core.management import call_command

        # setup temporary directory
        self.temp_dir = TemporaryDirectory()

        self.static_root = os.path.join(
            self.temp_dir.name,
            'django/static',
        )

        self.static_dir = os.path.join(
            self.static_root,
            self.STATIC_URL_PREFIX,
        )

        os.makedirs(self.static_dir)

        # django collect static
        logger.info('collecting Django static files')

        django_settings.STATIC_ROOT = self.static_dir

        django_settings.STATIC_URL = os.path.join(
            django_settings.STATIC_URL,
            self.STATIC_URL_PREFIX,
        )

        call_command('collectstatic', '--no-input', '-v', '0')

        # count collected files
        logger.info(
            '%s files copied to %s',
            self.count_static_files(),
            self.static_root,
        )

        # add temp dir to lona static directories
        # FIXME: add proper API to Lona
        data.server._static_file_loader.static_dirs.append(self.static_root)
