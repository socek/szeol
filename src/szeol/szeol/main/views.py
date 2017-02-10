from functools import wraps

from django.shortcuts import render


def contextwrapper(method):
    @wraps(method)
    def wrapper(self, request, *args, **kwargs):
        request._context = self._context = getattr(request, '_context', {})
        self._request = request
        self._matchdict = kwargs
        self._request.menu_id = getattr(self, 'MENU_ID', '')
        result = method(
            self,
            request,
            self._context,
            self._matchdict,
            *args,
            **kwargs)
        if not result:
            return render(request, self.TEMPLATE_NAME, self._context)
        else:
            return result

    return wrapper
