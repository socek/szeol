from functools import wraps

from django.shortcuts import render


def contextwrapper(method):
    @wraps(method)
    def wrapper(self, request, *args, **kwargs):
        self._context = {}
        self._request = request
        self._matchdict = kwargs
        method(self, request, self._context, self._matchdict, *args, **kwargs)
        return render(request, self.TEMPLATE_NAME, self._context)

    return wrapper
