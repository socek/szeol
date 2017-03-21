from mock import patch
from mock import sentinel

from django.conf import settings
from pytest import yield_fixture

from szeol.main.testing import SzeolDriverFixtures
from szeol.main.testing import SzeolFixtures
from szeol.contacts.views import CreateContact
from szeol.contacts.views import EditContact
from szeol.contacts.views import ListContact


class TestDashboardHome(SzeolFixtures):

    MAINPATH = 'szeol.contacts.views'

    @yield_fixture
    def mform(self):
        with self._patch('CreateContactForm') as mock:
            yield mock

    def test_get(self, mrequest, mform):
        ctrl = CreateContact()

        result = ctrl.get(mrequest)

        assert result.status_code == 200
        mform.assert_called_once_with()
        mrequest._context == dict(form=mform.return_value)

    def test_post_on_fail(self, mrequest, mform):
        ctrl = CreateContact()
        mform.return_value.is_valid.return_value = False

        result = ctrl.post(mrequest)

        assert result.status_code == 200
        mform.assert_called_once_with(mrequest.POST)
        mrequest._context == dict(form=mform.return_value)

    def test_post_on_success(self, mrequest, mform, mredirect):
        ctrl = CreateContact()
        mform.return_value.is_valid.return_value = True

        result = ctrl.post(mrequest)

        assert result == mredirect.return_value
        mform.assert_called_once_with(mrequest.POST)
        mredirect.assert_called_once_with('contacts_list')


class TestListContact(SzeolDriverFixtures):

    def test_get(self, mrequest, mcontact_driver):
        ctrl = ListContact()

        ctrl.get(mrequest)

        mrequest._context == dict(
            contacts=mcontact_driver.viewable.return_value,
            settings=settings)


class TestEditContact(SzeolDriverFixtures):

    MAINPATH = 'szeol.contacts.views'

    @yield_fixture
    def medit_contact_form(self):
        with patch('szeol.contacts.views.EditContactForm') as mock:
            yield mock

    @yield_fixture
    def mfetch_contact(self):
        with patch.object(EditContact, '_fetch_contact') as mock:
            yield mock

    @yield_fixture
    def mfetch_form(self):
        with patch.object(EditContact, '_fetch_form') as mock:
            yield mock

    def test_fetch_contact(self, mcontact_driver):
        ctrl = EditContact()

        context = dict()
        matchdict = dict(contact_id=sentinel.contact_id)

        result = ctrl._fetch_contact(context, matchdict)

        assert result == mcontact_driver.get_viewable_by_id.return_value
        mcontact_driver.get_viewable_by_id.assert_called_once_with(
            sentinel.contact_id)
        assert context == dict(contact=result)

    def test_fetch_form(self, medit_contact_form):
        ctrl = EditContact()

        context = dict()
        contact = sentinel.contact
        post = sentinel.post

        result = ctrl._fetch_form(context, contact, post)

        medit_contact_form.assert_called_once_with(post, instance=contact)
        assert context == dict(form=medit_contact_form.return_value)
        assert result == medit_contact_form.return_value

    def test_get(self, mrequest, mfetch_contact, mfetch_form):
        ctrl = EditContact()

        ctrl.get(mrequest)

        mfetch_contact.assert_called_once_with(
            mrequest._context,
            mrequest._matchdict)
        mfetch_form.assert_called_once_with(
            mrequest._context,
            mfetch_contact.return_value)

    def test_post_fail(
        self,
        mrequest,
        mfetch_contact,
        mfetch_form,
    ):
        ctrl = EditContact()
        form = mfetch_form.return_value
        form.is_valid.return_value = False

        ctrl.post(mrequest)

        mfetch_contact.assert_called_once_with(
            mrequest._context,
            mrequest._matchdict)
        mfetch_form.assert_called_once_with(
            mrequest._context,
            mfetch_contact.return_value,
            mrequest.POST)

        form.is_valid.assert_called_once_with()

    def test_post_success(
        self,
        mrequest,
        mfetch_contact,
        mfetch_form,
        mredirect,
    ):
        ctrl = EditContact()
        form = mfetch_form.return_value
        form.is_valid.return_value = True

        result = ctrl.post(mrequest)

        mfetch_contact.assert_called_once_with(
            mrequest._context,
            mrequest._matchdict)
        mfetch_form.assert_called_once_with(
            mrequest._context,
            mfetch_contact.return_value,
            mrequest.POST)

        form.is_valid.assert_called_once_with()
        form.save.assert_called_once_with()
        assert result == mredirect.return_value
        mredirect.assert_called_once_with('contacts_list')
