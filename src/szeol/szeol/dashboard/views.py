from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from szeol.contacts.models import Contact
from szeol.main.views import ContextWrapper
from szeol.orders.models import Order
from szeol.products.models import Product


class DashboardHome(LoginRequiredMixin, View):

    MENU_ID = 'dashboard_home'
    TEMPLATE_NAME = 'szeol/dashboard.html'

    @ContextWrapper()
    def get(self, request, context, matchdict):
        context['statistics'] = self.get_statistics()

    def get_statistics(self):
        return dict(
            products=Product.Driver.viewable_count(),
            products_created=Product.Driver.last_week_created_count(),
            contacts=Contact.Driver.viewable_count(),
            contacts_created=Contact.Driver.last_week_created_count(),
            orders=Order.Driver.viewable_count(),
            orders_created=Order.Driver.last_week_created_count(),
        )
