from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(
        r'^accounts/',
        include('szeol.localauth.urls')),
    url(
        r'^',
        include('szeol.dashboard.urls')),
]
