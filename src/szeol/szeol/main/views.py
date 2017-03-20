from functools import wraps

from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings


class ContextWrapper(object):

    def __call__(self, method):
        @wraps(method)
        def wrapper(mself, request, *args, **kwargs):
            context = self.init_context(mself, request)
            matchdict = self.init_matchdict(mself, request, kwargs)
            self.init_menu(mself, request)

            result = method(
                mself,
                request,
                context,
                matchdict,
                *args)
            if not result:
                return self.default_render(mself, request)
            else:
                return result

        return wrapper

    def init_context(self, mself, request):
        context = getattr(request, '_context', None)
        if not context:
            request._context = {
                'settings': settings,
            }
        return request._context

    def init_matchdict(self, mself, request, kwargs):
        matchdict = getattr(request, '_matchdict', None)
        if not matchdict:
            request._matchdict = kwargs
        return request._matchdict

    def init_menu(self, mself, request):
        request.menu_id = getattr(mself, 'MENU_ID', '')

    def default_render(self, mself, request):
        return render(request, mself.TEMPLATE_NAME, request._context)


class JsonContextWrapper(ContextWrapper):

    def init_context(self, mself, request):
        context = getattr(request, '_context', None)
        if not context:
            request._context = dict()
        return request._context

    def default_render(self, mself, request):
        return JsonResponse(request._context)
