from mock import MagicMock
from mock import patch
from pytest import fixture
from pytest import yield_fixture


class SzeolFixtures(object):

    MAINPATH = ''

    def _patch(self, name, *args, **kwargs):
        return patch(self.MAINPATH + '.' + name, *args, **kwargs)

    @fixture
    def mrequest(self):
        return MagicMock()

    @yield_fixture
    def mredirect(self):
        with self._patch('redirect') as mock:
            yield mock
