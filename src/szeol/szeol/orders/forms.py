from django.forms import ModelForm

from szeol.orders.models import Order


class CreateOrderForm(ModelForm):

    class Meta:
        model = Order
        exclude = ['when_created']

    def to_dict(self):
        data = dict(fields={})
        for field in self:
            data['fields'][field.name] = dict(
                value=field.value(),
                name=field.name,
                errros=field.errors,
            )
        return data


class EditOrderForm(ModelForm):

    class Meta:
        model = Order
        exclude = ['when_created', 'address']
