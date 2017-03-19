from functools import wraps

from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings


def contextwrapper(method):
    @wraps(method)
    def wrapper(self, request, *args, **kwargs):
        context = getattr(request, '_context', None)
        if not context:
            context = {
                'settings': settings,
            }
        request._context = self._context = context
        self._request = request
        self._matchdict = kwargs
        self._request.menu_id = getattr(self, 'MENU_ID', '')
        result = method(
            self,
            request,
            self._context,
            self._matchdict,
            *args)
        if not result:
            return render(request, self.TEMPLATE_NAME, self._context)
        else:
            return result

    return wrapper


def jsonwrapper(method):
    @wraps(method)
    def wrapper(self, request, *args, **kwargs):
        json = request._json = self._json = getattr(request, '_json', {})
        self._request = request
        self._matchdict = kwargs
        result = method(
            self,
            request,
            json,
            self._matchdict,
            *args)
        if not result:
            return JsonResponse(json)
        else:
            return result

    return wrapper
