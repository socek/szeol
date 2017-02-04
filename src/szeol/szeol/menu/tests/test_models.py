from mock import MagicMock
from mock import sentinel

from szeol.main.testing import SzeolFixtures
from szeol.menu.models import DownMenuObject
from szeol.menu.models import MenuParser
from szeol.menu.models import TopMenuObject


class TestDownMenuObject(SzeolFixtures):

    def test_init(self, mrequest):
        data = dict(id='myid', name='myname', url=lambda: 'myurl')
        obj = DownMenuObject(mrequest, data)
        assert obj.id == 'myid'
        assert obj.name == 'myname'
        assert obj.url() == 'myurl'
        assert obj.request == mrequest

    def test_is_active(self, mrequest):
        data = dict(id='myid', name='myname', url=lambda: 'myurl')
        obj = DownMenuObject(mrequest, data)

        mrequest.menu_id = 'myid'
        assert obj.is_active

        mrequest.menu_id = 'notmyid'
        assert not obj.is_active


class TestTopMenuObject(SzeolFixtures):

    def test_init(self, mrequest):
        data = dict(id='myid', name='myname', icon='myicon')
        obj = TopMenuObject(mrequest, data, sentinel.elements)
        assert obj.id == 'myid'
        assert obj.name == 'myname'
        assert obj.icon == 'myicon'
        assert obj.elements == sentinel.elements
        assert obj.request == mrequest

    def test_is_active(self, mrequest):
        elements = [MagicMock(), MagicMock]
        data = dict(id='myid', name='myname')
        obj = TopMenuObject(mrequest, data, elements)

        elements[0].is_active = False
        elements[1].is_active = False
        assert not obj.is_active

        elements[0].is_active = False
        elements[1].is_active = True
        assert obj.is_active
