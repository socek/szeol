from mock import MagicMock
from pytest import fixture


class SzeolFixtures(object):

    @fixture
    def mrequest(self):
        return MagicMock()
