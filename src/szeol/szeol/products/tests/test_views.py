from mock import patch
from mock import sentinel

from django.conf import settings
from pytest import yield_fixture

from szeol.main.testing import SzeolDriverFixtures
from szeol.main.testing import SzeolFixtures
from szeol.products.views import CreateProduct
from szeol.products.views import EditProduct
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
        mrequest._context == dict(form=mform.return_value)

    def test_post_on_fail(self, mrequest, mform):
        ctrl = CreateProduct()
        mform.return_value.is_valid.return_value = False

        result = ctrl.post(mrequest)

        assert result.status_code == 200
        mform.assert_called_once_with(mrequest.POST)
        mrequest._context == dict(form=mform.return_value)

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

        mrequest._context == dict(
            products=mproduct_driver.viewable.return_value,
            settings=settings)


class TestEditProduct(SzeolDriverFixtures):

    MAINPATH = 'szeol.products.views'

    @yield_fixture
    def medit_product_form(self):
        with patch('szeol.products.views.EditProductForm') as mock:
            yield mock

    @yield_fixture
    def mfetch_product(self):
        with patch.object(EditProduct, '_fetch_product') as mock:
            yield mock

    @yield_fixture
    def mfetch_form(self):
        with patch.object(EditProduct, '_fetch_form') as mock:
            yield mock

    def test_fetch_product(self, mproduct_driver):
        ctrl = EditProduct()

        context = dict()
        matchdict = dict(product_id=sentinel.product_id)

        result = ctrl._fetch_product(context, matchdict)

        assert result == mproduct_driver.get_viewable_by_id.return_value
        mproduct_driver.get_viewable_by_id.assert_called_once_with(
            sentinel.product_id)
        assert context == dict(product=result)

    def test_fetch_form(self, medit_product_form):
        ctrl = EditProduct()

        context = dict()
        product = sentinel.product
        post = sentinel.post

        result = ctrl._fetch_form(context, product, post)

        medit_product_form.assert_called_once_with(post, instance=product)
        assert context == dict(form=medit_product_form.return_value)
        assert result == medit_product_form.return_value

    def test_get(self, mrequest, mfetch_product, mfetch_form):
        ctrl = EditProduct()

        ctrl.get(mrequest)

        mfetch_product.assert_called_once_with(
            mrequest._context,
            mrequest._matchdict)
        mfetch_form.assert_called_once_with(
            mrequest._context,
            mfetch_product.return_value)

    def test_post_fail(
        self,
        mrequest,
        mfetch_product,
        mfetch_form,
    ):
        ctrl = EditProduct()
        form = mfetch_form.return_value
        form.is_valid.return_value = False

        ctrl.post(mrequest)

        mfetch_product.assert_called_once_with(
            mrequest._context,
            mrequest._matchdict)
        mfetch_form.assert_called_once_with(
            mrequest._context,
            mfetch_product.return_value,
            mrequest.POST)

        form.is_valid.assert_called_once_with()

    def test_post_success(
        self,
        mrequest,
        mfetch_product,
        mfetch_form,
        mredirect,
    ):
        ctrl = EditProduct()
        form = mfetch_form.return_value
        form.is_valid.return_value = True

        result = ctrl.post(mrequest)

        mfetch_product.assert_called_once_with(
            mrequest._context,
            mrequest._matchdict)
        mfetch_form.assert_called_once_with(
            mrequest._context,
            mfetch_product.return_value,
            mrequest.POST)

        form.is_valid.assert_called_once_with()
        form.save.assert_called_once_with()
        assert result == mredirect.return_value
        mredirect.assert_called_once_with('products_list')
