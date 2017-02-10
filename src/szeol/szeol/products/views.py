from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from szeol.main.views import contextwrapper
from szeol.products.forms import CreateProductForm
from szeol.products.models import Product


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
            return redirect('products_list')

        context['form'] = form


class ListProduct(LoginRequiredMixin, View):

    MENU_ID = 'products_list'
    TEMPLATE_NAME = 'products/list.html'

    @contextwrapper
    def get(self, request, context, matchdict):
        context['products'] = Product.Driver.viewable()
