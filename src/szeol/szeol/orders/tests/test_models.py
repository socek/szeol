from datetime import datetime
from datetime import timedelta
from freezegun import freeze_time
from pytest import fixture
from pytest import mark
from pytest import raises

from szeol.orders.models import Order
# from szeol.orders.models import OrderItem


@mark.django_db
class TestOrderDriver(object):

    @fixture
    def base_time(self):
        return datetime(2012, 1, 1)

    @fixture
    def order(self, base_time=None):
        base_time = self.base_time()
        with freeze_time(base_time):
            order = Order(
                description='description')
            order.save()
        return order

    def test_viewable(self):
        assert Order.Driver.viewable_count() == 0
        assert list(Order.Driver.viewable()) == []

        order = self.order()
        assert Order.Driver.viewable_count() == 1
        assert Order.Driver.viewable()[0].id == order.id

        order = self.order()
        assert Order.Driver.viewable_count() == 2
        assert Order.Driver.viewable()[1].id == order.id

    def test_get_viewable_by_id(self):
        with raises(Order.DoesNotExist):
            Order.Driver.get_viewable_by_id(1)

        order = self.order()

        assert Order.Driver.get_viewable_by_id(order.id) == order

    @mark.parametrize(
        "days",
        range(8)
    )
    def test_last_week_created(self, days, base_time, order):
        now = base_time + timedelta(days=days)
        with freeze_time(now):
            expected_count = 1 if days <= 7 else 0
            assert Order.Driver.last_week_created_count() == expected_count
