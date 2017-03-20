from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from szeol.main.views import ContextWrapper
from szeol.contacts.forms import CreateContactForm
from szeol.contacts.forms import EditContactForm
from szeol.contacts.models import Contact


class CreateContact(LoginRequiredMixin, View):

    MENU_ID = 'contacts_create'
    TEMPLATE_NAME = 'contacts/create.html'

    @ContextWrapper()
    def get(self, request, context, matchdict):
        context['form'] = CreateContactForm()

    @ContextWrapper()
    def post(self, request, context, matchdict):
        form = CreateContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')

        context['form'] = form


class ListContact(LoginRequiredMixin, View):

    MENU_ID = 'contacts_list'
    TEMPLATE_NAME = 'contacts/list.html'

    @ContextWrapper()
    def get(self, request, context, matchdict):
        context['contacts'] = Contact.Driver.viewable()


class EditContact(LoginRequiredMixin, View):

    MENU_ID = 'contacts_list'
    TEMPLATE_NAME = 'contacts/edit.html'

    @ContextWrapper()
    def get(self, request, context, matchdict):
        contact = self._fetch_contact(context, matchdict)
        self._fetch_form(context, contact)

    @ContextWrapper()
    def post(self, request, context, matchdict):
        contact = self._fetch_contact(context, matchdict)
        form = self._fetch_form(context, contact, request.POST)

        if form.is_valid():
            form.save()
            return redirect('contacts_list')

    def _fetch_contact(self, context, matchdict):
        contact = Contact.Driver.get_viewable_by_id(
            matchdict['contact_id'])
        context['contact'] = contact
        return contact

    def _fetch_form(self, context, contact, post=None):
        form = EditContactForm(post, instance=contact)
        context['form'] = form
        return form
