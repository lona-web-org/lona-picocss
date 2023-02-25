import traceback
import html
import sys

from lona import View, ForbiddenError
from lona_picocss import settings


class Error403View(View):
    def handle_request(self, request, exception):
        if not request.interactive:
            return {
                'template': 'picocss/base.html',
                'request': request,
            }

        message = 'Forbidden'

        if exception.args:
            message = exception.args[0]

        return f"""
            <h1>Error 403</h1>
            <p>{message}</p>
        """


class Error404View(View):
    def handle_request(self, request):
        if request.url.path == '/':
            return {
                'redirect': self.server.reverse('picocss__it_works'),
            }

        if request.interactive:
            return """
                <h1>Error 404</h1>
                <p>Not Found</p>
            """

        return {
            'template': 'picocss/base.html',
            'request': request,
        }


class Error500View(View):
    def format_exception(self, exception):
        if sys.version_info >= (3, 10):
            lines = traceback.format_exception(exception)

        else:
            lines = traceback.format_exception(
                etype=type(exception),
                value=exception,
                tb=exception.__traceback__,
            )

        return html.escape(''.join(lines))

    def handle_request(self, request, exception):
        if request.interactive:
            show_exceptions = self.server.settings.get(
                'PICOCSS_SHOW_EXCEPTIONS',
                settings.DEFAULTS['PICOCSS_SHOW_EXCEPTIONS'],
            )

            if show_exceptions:
                return f"""
                    <h1>Error 500</h1>
                    <p>Internal Error</p>
                    <pre>{self.format_exception(exception)}</pre>
                """

            return """
                <h1>Error 500</h1>
                <p>Internal Error</p>
            """

        return {
            'template': 'picocss/base.html',
            'request': request,
        }


class InternalErrorView(View):
    def handle_request(self, request):
        raise RuntimeError('Internal Error')


class ForbiddenErrorView(View):
    def handle_request(self, request):
        raise ForbiddenError()
