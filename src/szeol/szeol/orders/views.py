from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from szeol.main.views import ContextWrapper
from szeol.orders.models import Order


class ListOrder(LoginRequiredMixin, View):

    MENU_ID = 'orders_list'
    TEMPLATE_NAME = 'orders/list.html'

    @ContextWrapper()
    def get(self, request, context, matchdict):
        context['orders'] = Order.Driver.viewable_tab()
