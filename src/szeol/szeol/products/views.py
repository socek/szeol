from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from szeol.main.views import contextwrapper
from szeol.products.forms import CreateProductForm


class CreateProduct(LoginRequiredMixin, View):

    MENU_ID = 'products_create'
    TEMPLATE_NAME = 'products/create.html'

    @contextwrapper
    def get(self, request, context, matchdict):
        context['form'] = CreateProductForm()

    @contextwrapper
    def post(self, request, context, matchdict):
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')

        context['form'] = form
