from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from szeol.main.views import ContextWrapper
from szeol.main.views import JsonContextWrapper
from szeol.orders.forms import CreateOrderForm
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
        context['form'] = CreateOrderForm()

    @JsonContextWrapper()
    def options(self, request, context, matchdict):
        context['form'] = CreateOrderForm().to_dict()

    @JsonContextWrapper()
    def post(self, request, context, matchdict):
        form = CreateOrderForm(request.POST)
        is_valid = form.is_valid()

        if is_valid:
            form.save()
        context['form'] = form.to_dict()
        context['is_valid'] = is_valid
