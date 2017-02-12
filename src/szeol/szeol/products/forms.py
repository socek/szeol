from django.forms import ModelForm

from szeol.products.models import Product


class CreateProductForm(ModelForm):

    class Meta:
        model = Product
        exclude = ['when_created']


class EditProductForm(ModelForm):

    class Meta:
        model = Product
        exclude = ['when_created']
