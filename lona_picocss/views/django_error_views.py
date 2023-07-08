import sys


def handler403(request, exception=None):
    from django.shortcuts import render

    return render(request, 'picocss/django/403.html', {
        'exception': exception,
    }, status=403)


def handler404(request, exception=None):
    from django.shortcuts import render

    return render(request, 'picocss/django/404.html', {
        'exception': exception,
    }, status=404)


def handler500(request, exception=None):
    from django.shortcuts import render

    exception = exception or sys.exc_info()[1]

    return render(request, 'picocss/django/500.html', {
        'exception': exception,
    }, status=500)
