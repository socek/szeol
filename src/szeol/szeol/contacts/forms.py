from django.forms import ModelForm

from szeol.contacts.models import Contact


class CreateContactForm(ModelForm):

    class Meta:
        model = Contact
        exclude = ['when_created', 'address']


class EditContactForm(ModelForm):

    class Meta:
        model = Contact
        exclude = ['when_created', 'address']
