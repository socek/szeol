from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from szeol.main.views import ContextWrapper
from szeol.products.forms import CreateProductForm
from szeol.products.forms import EditProductForm
from szeol.products.models import Product


class CreateProduct(LoginRequiredMixin, View):

    MENU_ID = 'products_create'
    TEMPLATE_NAME = 'products/create.html'

    @ContextWrapper()
    def get(self, request, context, matchdict):
        context['form'] = CreateProductForm()

    @ContextWrapper()
    def post(self, request, context, matchdict):
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')

        context['form'] = form


class ListProduct(LoginRequiredMixin, View):

    MENU_ID = 'products_list'
    TEMPLATE_NAME = 'products/list.html'

    @ContextWrapper()
    def get(self, request, context, matchdict):
        context['products'] = Product.Driver.viewable()


class EditProduct(LoginRequiredMixin, View):

    MENU_ID = 'products_list'
    TEMPLATE_NAME = 'products/edit.html'

    @ContextWrapper()
    def get(self, request, context, matchdict):
        product = self._fetch_product(context, matchdict)
        self._fetch_form(context, product)

    @ContextWrapper()
    def post(self, request, context, matchdict):
        product = self._fetch_product(context, matchdict)
        form = self._fetch_form(context, product, request.POST)

        if form.is_valid():
            form.save()
            return redirect('products_list')

    def _fetch_product(self, context, matchdict):
        product = Product.Driver.get_viewable_by_id(
            matchdict['product_id'])
        context['product'] = product
        return product

    def _fetch_form(self, context, product, post=None):
        form = EditProductForm(post, instance=product)
        context['form'] = form
        return form
