from django.conf.urls import url

from .views import CreateOrder
from .views import ListOrder


urlpatterns = [
    url(
        r'^create/$',
        CreateOrder.as_view(),
        name='orders_create'),
    url(
        r'^$',
        ListOrder.as_view(),
        name='orders_list'),
]
