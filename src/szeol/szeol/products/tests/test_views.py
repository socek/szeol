from pytest import yield_fixture

from szeol.main.testing import SzeolDriverFixtures
from szeol.main.testing import SzeolFixtures
from szeol.products.views import CreateProduct
from szeol.products.views import ListProduct


class TestDashboardHome(SzeolFixtures):

    MAINPATH = 'szeol.products.views'

    @yield_fixture
    def mform(self):
        with self._patch('CreateProductForm') as mock:
            yield mock

    def test_get(self, mrequest, mform):
        ctrl = CreateProduct()

        result = ctrl.get(mrequest)

        assert result.status_code == 200
        mform.assert_called_once_with()
        ctrl._context == dict(form=mform.return_value)

    def test_post_on_fail(self, mrequest, mform):
        ctrl = CreateProduct()
        mform.return_value.is_valid.return_value = False

        result = ctrl.post(mrequest)

        assert result.status_code == 200
        mform.assert_called_once_with(mrequest.POST)
        ctrl._context == dict(form=mform.return_value)

    def test_post_on_success(self, mrequest, mform, mredirect):
        ctrl = CreateProduct()
        mform.return_value.is_valid.return_value = True

        result = ctrl.post(mrequest)

        assert result == mredirect.return_value
        mform.assert_called_once_with(mrequest.POST)
        mredirect.assert_called_once_with('products_list')


class TestListProduct(SzeolDriverFixtures):

    def test_get(self, mrequest, mproduct_driver):
        ctrl = ListProduct()

        ctrl.get(mrequest)

        assert ctrl._context == dict(
            products=mproduct_driver.viewable.return_value)
