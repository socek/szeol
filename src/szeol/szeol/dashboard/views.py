from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from szeol.main.views import contextwrapper
from szeol.products.models import Product


class DashboardHome(LoginRequiredMixin, View):

    MENU_ID = 'dashboard_home'
    TEMPLATE_NAME = 'szeol/dashboard.html'

    @contextwrapper
    def get(self, request, context, matchdict):
        context['statistics'] = self.get_statistics()

    def get_statistics(self):
        return dict(
            products=Product.Driver.viewable_count(),
            products_created=Product.Driver.last_week_created_count()
        )
