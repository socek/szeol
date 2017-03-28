from django.forms import ModelForm

from szeol.orders.models import Order


class CreateOrderForm(ModelForm):

    class Meta:
        model = Order
        exclude = ['when_created', 'address']


class EditOrderForm(ModelForm):

    class Meta:
        model = Order
        exclude = ['when_created', 'address']
