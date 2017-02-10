from datetime import datetime
from datetime import timedelta
from freezegun import freeze_time
from pytest import fixture
from pytest import mark

from szeol.products.models import Product


class TestProduct(object):

    @mark.parametrize(
        "value, name",
        Product.TASTES,
    )
    def test_tastes(self, value, name):
        product = Product(taste=value)
        assert product.taste_name == name

    @mark.parametrize(
        "value, name",
        Product.COLORS,
    )
    def test_color(self, value, name):
        product = Product(color=value)
        assert product.color_name == name


@mark.django_db
class TestProductDriver(object):

    @fixture
    def base_time(self):
        return datetime(2012, 1, 1)

    @fixture
    def product(self, base_time=None):
        base_time = self.base_time()
        with freeze_time(base_time):
            product = Product(
                name='wine',
                year='1986',
                taste='d',
                color='wh')
            product.save()
        return product

    def test_viewable(self):
        assert Product.Driver.viewable_count() == 0
        assert list(Product.Driver.viewable()) == []

        product = self.product()
        assert Product.Driver.viewable_count() == 1
        assert Product.Driver.viewable()[0].id == product.id

        product = self.product()
        assert Product.Driver.viewable_count() == 2
        assert Product.Driver.viewable()[1].id == product.id

    @mark.parametrize(
        "days",
        range(8)
    )
    def test_last_week_created(self, days, base_time, product):
        now = base_time + timedelta(days=days)
        with freeze_time(now):
            expected_count = 1 if days <= 7 else 0
            assert Product.Driver.last_week_created_count() == expected_count
