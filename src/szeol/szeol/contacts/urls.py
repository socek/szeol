from django.conf.urls import url

from .views import CreateContact
from .views import EditContact
from .views import ListContact


urlpatterns = [
    url(
        r'^create/$',
        CreateContact.as_view(),
        name='contacts_create'),
    url(
        r'^$',
        ListContact.as_view(),
        name='contacts_list'),
    url(
        r'^edit/(?P<contact_id>[0-9]+)/$',
        EditContact.as_view(),
        name='contacts_edit'),
]
