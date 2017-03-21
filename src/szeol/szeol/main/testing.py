from mock import MagicMock
from mock import patch
from pytest import fixture
from pytest import yield_fixture

from szeol.contacts.models import Contact
from szeol.products.models import Product


class SzeolFixtures(object):

    MAINPATH = ''

    def _patch(self, name, *args, **kwargs):
        return patch(self.MAINPATH + '.' + name, *args, **kwargs)

    @fixture
    def mrequest(self):
        mock = MagicMock()
        mock._context = {}
        return mock

    @yield_fixture
    def mredirect(self):
        with self._patch('redirect') as mock:
            yield mock

    @yield_fixture
    def mrender(self):
        with self._patch('render') as mock:
            yield mock


class SzeolDriverFixtures(SzeolFixtures):

    @yield_fixture
    def mproduct_driver(self):
        with patch.object(Product, 'Driver') as mock:
            yield mock

    @yield_fixture
    def mcontact_driver(self):
        with patch.object(Contact, 'Driver') as mock:
            yield mock
