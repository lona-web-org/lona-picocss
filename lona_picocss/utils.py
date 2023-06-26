import traceback
import html
import sys


def exception_to_html(exception):
    if sys.version_info >= (3, 10):
        lines = traceback.format_exception(exception)

    else:
        lines = traceback.format_exception(
            etype=type(exception),
            value=exception,
            tb=exception.__traceback__,
        )

    return html.escape(''.join(lines))


def get_django_show_exceptions(server, request):
    return request.user.is_staff
