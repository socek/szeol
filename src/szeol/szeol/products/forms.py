from django.forms import ModelForm

from szeol.products.models import Product


class CreateProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'year', 'taste', 'color']
