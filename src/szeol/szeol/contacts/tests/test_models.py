from datetime import datetime
from datetime import timedelta
from freezegun import freeze_time
from pytest import fixture
from pytest import mark
from pytest import raises

from szeol.contacts.models import Contact


@mark.django_db
class TestContactDriver(object):

    @fixture
    def base_time(self):
        return datetime(2012, 1, 1)

    @fixture
    def contact(self, base_time=None):
        base_time = self.base_time()
        with freeze_time(base_time):
            contact = Contact(
                name='adam',
                surname='kowalski',
                address='xxxx')
            contact.save()
        return contact

    def test_viewable(self):
        assert Contact.Driver.viewable_count() == 0
        assert list(Contact.Driver.viewable()) == []

        contact = self.contact()
        assert Contact.Driver.viewable_count() == 1
        assert Contact.Driver.viewable()[0].id == contact.id

        contact = self.contact()
        assert Contact.Driver.viewable_count() == 2
        assert Contact.Driver.viewable()[1].id == contact.id

    def test_get_viewable_by_id(self):
        with raises(Contact.DoesNotExist):
            Contact.Driver.get_viewable_by_id(1)

        contact = self.contact()

        assert Contact.Driver.get_viewable_by_id(contact.id) == contact

    @mark.parametrize(
        "days",
        range(8)
    )
    def test_last_week_created(self, days, base_time, contact):
        now = base_time + timedelta(days=days)
        with freeze_time(now):
            expected_count = 1 if days <= 7 else 0
            assert Contact.Driver.last_week_created_count() == expected_count
