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


class CreateOrder(LoginRequiredMixin, View):

    MENU_ID = 'orders_create'
    TEMPLATE_NAME = 'orders/create.html'

    @ContextWrapper()
    def get(self, request, context, matchdict):
        pass
        # context['form'] = CreateOrderForm()

    # @ContextWrapper()
    # def post(self, request, context, matchdict):
    #     form = CreateOrderForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('Orders_list')

    #     context['form'] = form
