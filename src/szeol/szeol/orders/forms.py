from django.forms import ModelForm
from django.forms import ValidationError

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
                errors=list(field.errors),
                is_valid=not bool(field.errors)
            )
            # print(field.name, data['fields'][field.name])
        return data

    def clean_discount(self):
        data = self.cleaned_data['discount']
        if int(data) < 1:
            raise ValidationError("You have forgotten about Fred!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data


class EditOrderForm(ModelForm):

    class Meta:
        model = Order
        exclude = ['when_created', 'address']
