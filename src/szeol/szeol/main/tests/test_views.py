from django.conf import settings
from mock import MagicMock
from mock import call
from mock import sentinel
from pytest import yield_fixture

from szeol.main.testing import SzeolFixtures
from szeol.main.views import ContextWrapper
from szeol.main.views import JsonContextWrapper


class TestContextWrapper(SzeolFixtures):
    MAINPATH = 'szeol.main.views'
    TEMPLATE_NAME = sentinel.template_name

    @ContextWrapper()
    def _samle_method(self, request, context, matchdict, additional):
        request._result = dict(
            context=context,
            matchdict=matchdict,
            additional=additional)

    @ContextWrapper()
    def _non_default_samle_method(self, request, context, matchdict):
        return sentinel.non_default_return

    def test_normal(self, mrender):
        request = MagicMock()
        request._context = None
        request._matchdict = None

        result = self._samle_method(request, sentinel.additional, himon=10)

        assert request._result['context'] is request._context
        assert request._result['context'] == dict(
            settings=settings)
        assert request._result['matchdict'] is request._matchdict
        assert request._result['additional'] == sentinel.additional

        assert result == mrender.return_value
        mrender.assert_called_once_with(
            request,
            sentinel.template_name,
            request._context)

    def test_double_initalization(self, mrender):
        request = MagicMock()
        request._context = None
        request._matchdict = None

        result = self._samle_method(request, sentinel.additional)
        request._result['context']['something'] = sentinel.something
        result = self._samle_method(request, sentinel.additional)

        assert request._result['context'] is request._context
        assert request._result['context'] == dict(
            settings=settings,
            something=sentinel.something)
        assert request._result['matchdict'] is request._matchdict
        assert request._result['additional'] == sentinel.additional

        assert result == mrender.return_value
        assert mrender.call_args_list == [
            call(
                request,
                sentinel.template_name,
                request._context),
            call(
                request,
                sentinel.template_name,
                request._context),
        ]

    def test_non_default_return(self):
        request = MagicMock()
        assert self._non_default_samle_method(request) == sentinel.non_default_return


class TestJsonContextWrapper(SzeolFixtures):
    MAINPATH = 'szeol.main.views'

    @yield_fixture
    def mjson_response(self):
        with self._patch('JsonResponse') as mock:
            yield mock

    @JsonContextWrapper()
    def _samle_method(self, request, context, matchdict, additional):
        request._result = dict(
            context=context,
            matchdict=matchdict,
            additional=additional)

    def test_normal(self, mjson_response):
        request = MagicMock()
        request._context = None
        request._matchdict = None

        result = self._samle_method(request, sentinel.additional, himon=10)

        assert request._result['context'] is request._context
        assert request._result['context'] == dict()
        assert request._result['matchdict'] is request._matchdict
        assert request._result['additional'] == sentinel.additional

        assert result == mjson_response.return_value
        mjson_response.assert_called_once_with(request._context)

    def test_double_initalization(self, mjson_response):
        request = MagicMock()
        request._context = None
        request._matchdict = None

        result = self._samle_method(request, sentinel.additional, himon=10)
        request._result['context']['something'] = sentinel.something
        result = self._samle_method(request, sentinel.additional)

        assert request._result['context'] is request._context
        assert request._result['context'] == dict(
            something=sentinel.something)
        assert request._result['matchdict'] is request._matchdict
        assert request._result['additional'] == sentinel.additional

        assert result == mjson_response.return_value
        assert mjson_response.call_args_list == [
            call(request._context),
            call(request._context),
        ]
