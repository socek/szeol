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


class TestMenuParser(SzeolFixtures):
    MENU = (
        dict(
            id='dashboard',
            name='Dashboard',
            icon='fa-home',
            elements=(
                dict(
                    id='dashboard_home',
                    name='Statistics',
                    url=lambda: 'someurl',
                ),
            )
        ),
    )

    def test_simple(self, mrequest):
        menu = MenuParser(self.MENU)
        menu.TOP_MENU_CLS = MagicMock()
        menu.DOWN_MENU_CLS = MagicMock()

        data = list(menu.parse(mrequest))

        assert len(data) == 1
        assert data[0] == menu.TOP_MENU_CLS.return_value
        menu.TOP_MENU_CLS.assert_called_once_with(
            mrequest,
            self.MENU[0],
            [menu.DOWN_MENU_CLS.return_value])
        menu.DOWN_MENU_CLS.assert_called_once_with(
            mrequest,
            self.MENU[0]['elements'][0])
