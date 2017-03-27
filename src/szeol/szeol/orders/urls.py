from django.conf.urls import url

from .views import ListOrder


urlpatterns = [
    url(
        r'^$',
        ListOrder.as_view(),
        name='orders_list'),
]
