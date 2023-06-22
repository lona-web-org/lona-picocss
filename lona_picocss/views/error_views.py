from lona import (
    TemplateResponse,
    RedirectResponse,
    ForbiddenError,
    NotFoundError,
    View,
)


class Error403View(View):
    def handle_request(self, request, exception):
        if not request.interactive:
            return TemplateResponse('picocss/base.html', {
                'request': request,
            })

        message = 'Forbidden'

        if exception.args:
            message = exception.args[0]

        return TemplateResponse('picocss/403.html', {
            'request': request,
            'message': message,
        })


class Error404View(View):
    def handle_request(self, request):
        if request.url.path == '/':
            return RedirectResponse(self.server.reverse('picocss__it_works'))

        if request.interactive:
            return TemplateResponse('picocss/404.html', {
                'request': request,
            })

        return TemplateResponse('picocss/base.html', {
            'request': request,
        })


class Error500View(View):
    def handle_request(self, request, exception):
        if request.interactive:
            return TemplateResponse('picocss/500.html', {
                'request': request,
                'exception': exception,
            })

        return TemplateResponse('picocss/base.html', {
            'request': request,
        })


class ForbiddenErrorView(View):
    def handle_request(self, request):
        raise ForbiddenError()


class NotFoundErrorView(View):
    def handle_request(self, request):
        raise NotFoundError()


class InternalErrorView(View):
    def handle_request(self, request):
        raise RuntimeError('Internal Error')
