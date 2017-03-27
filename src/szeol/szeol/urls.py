from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(
        r'^accounts/',
        include('szeol.localauth.urls')),
    url(
        r'^products/',
        include('szeol.products.urls')),
    url(
        r'^contacts/',
        include('szeol.contacts.urls')),
    url(
        r'^orders/',
        include('szeol.orders.urls')),
    url(
        r'^',
        include('szeol.dashboard.urls')),
]
