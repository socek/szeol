from szeol.dashboard.views import DashboardHome
from szeol.main.testing import SzeolFixtures


class TestDashboardHome(SzeolFixtures):

    def test_get(self, mrequest):
        result = DashboardHome().get(mrequest)
        assert result.status_code == 200
