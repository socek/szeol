from django.conf import settings

from szeol.dashboard.views import DashboardHome
from szeol.main.testing import SzeolDriverFixtures


class TestDashboardHome(SzeolDriverFixtures):

    def test_get(self, mrequest, mproduct_driver):
        result = DashboardHome().get(mrequest)
        assert result.status_code == 200

        assert mrequest._context == dict(
            statistics=dict(
                products=mproduct_driver.viewable_count(),
                products_created=mproduct_driver.last_week_created_count()),
            settings=settings)
